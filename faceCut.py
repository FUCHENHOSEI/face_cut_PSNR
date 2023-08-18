# -*- coding: utf-8 -*-
import cv2
from mtcnn import MTCNN
import os
from datetime import datetime

# ��ʼ�� MTCNN ģ��
detector = MTCNN()

# ��ȡ�ļ����е�ͼƬ
folder_path = "fu_test"
image_files = os.listdir(folder_path)

# �����Ե�ǰʱ���������ļ���
output_folder = datetime.now().strftime("%Y%m%d%H%M%S")
os.makedirs(output_folder, exist_ok=True)

for image_file in image_files:
    # ��ȡͼƬ������ת��Ϊ RGB ��ʽ
    image_path = os.path.join(folder_path, image_file)
    image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

    # ��ԭʼͼƬ�ϼ������
    result = detector.detect_faces(image)

    if result:
        # ��ȡ������Ϣ
        bounding_box = result[0]['box']
        keypoints = result[0]['keypoints']

        # ��ͼ���ϻ��Ʊ߽��͹ؼ���
        image_with_keypoints = image.copy()
        cv2.rectangle(image_with_keypoints,
                      (bounding_box[0], bounding_box[1]),
                      (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
                      (0, 155, 255),
                      2)
        cv2.circle(image_with_keypoints, keypoints['left_eye'], 2, (0, 155, 255), 2)
        cv2.circle(image_with_keypoints, keypoints['right_eye'], 2, (0, 155, 255), 2)
        cv2.circle(image_with_keypoints, keypoints['nose'], 2, (0, 155, 255), 2)
        cv2.circle(image_with_keypoints, keypoints['mouth_left'], 2, (0, 155, 255), 2)
        cv2.circle(image_with_keypoints, keypoints['mouth_right'], 2, (0, 155, 255), 2)

        # ������б�ǵ�����ͼ��
        image_with_keypoints_path = os.path.join(output_folder, f"face_with_keypoints_{image_file}")
        cv2.imwrite(image_with_keypoints_path, cv2.cvtColor(image_with_keypoints, cv2.COLOR_RGB2BGR))

        # �ü�������������ͼ��
        face_only_image = image[bounding_box[1]:bounding_box[1] + bounding_box[3],
                                bounding_box[0]:bounding_box[0] + bounding_box[2]]

        # ���������������ͼ��
        face_only_path = os.path.join(output_folder, f"face_only_{image_file}")
        cv2.imwrite(face_only_path, cv2.cvtColor(face_only_image, cv2.COLOR_RGB2BGR))

        # ����ؼ���ͱ߽�����굽 txt �ļ�
        coordinates = {'left_eye': keypoints['left_eye'],
                       'right_eye': keypoints['right_eye'],
                       'nose': keypoints['nose'],
                       'mouth_left': keypoints['mouth_left'],
                       'mouth_right': keypoints['mouth_right'],
                       'bounding_box': bounding_box}

        coordinates_path = os.path.join(output_folder, f"face_coordinates_{image_file[:-4]}.txt")
        with open(coordinates_path, "w") as file:
            file.write(str(coordinates))

        # ������·��������̨
        print("Images and coordinates have been saved to folder:", output_folder)
        print(f"Image with keypoints ({image_file}):", image_with_keypoints_path)
        print(f"Face only image ({image_file}):", face_only_path)
        print(f"Face coordinates ({image_file}):", coordinates_path)
    else:
        print("No face detected in", image_file)