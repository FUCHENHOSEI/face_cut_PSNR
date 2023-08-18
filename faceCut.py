# -*- coding: utf-8 -*-
import cv2
from mtcnn import MTCNN
import os
from datetime import datetime

# 初始化 MTCNN 模型
detector = MTCNN()

# 读取文件夹中的图片
folder_path = "fu_test"
image_files = os.listdir(folder_path)

# 创建以当前时间命名的文件夹
output_folder = datetime.now().strftime("%Y%m%d%H%M%S")
os.makedirs(output_folder, exist_ok=True)

for image_file in image_files:
    # 读取图片并将其转换为 RGB 格式
    image_path = os.path.join(folder_path, image_file)
    image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

    # 在原始图片上检测人脸
    result = detector.detect_faces(image)

    if result:
        # 获取人脸信息
        bounding_box = result[0]['box']
        keypoints = result[0]['keypoints']

        # 在图像上绘制边界框和关键点
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

        # 保存带有标记的人脸图像
        image_with_keypoints_path = os.path.join(output_folder, f"face_with_keypoints_{image_file}")
        cv2.imwrite(image_with_keypoints_path, cv2.cvtColor(image_with_keypoints, cv2.COLOR_RGB2BGR))

        # 裁剪仅包含人脸的图像
        face_only_image = image[bounding_box[1]:bounding_box[1] + bounding_box[3],
                                bounding_box[0]:bounding_box[0] + bounding_box[2]]

        # 保存仅包含人脸的图像
        face_only_path = os.path.join(output_folder, f"face_only_{image_file}")
        cv2.imwrite(face_only_path, cv2.cvtColor(face_only_image, cv2.COLOR_RGB2BGR))

        # 保存关键点和边界框坐标到 txt 文件
        coordinates = {'left_eye': keypoints['left_eye'],
                       'right_eye': keypoints['right_eye'],
                       'nose': keypoints['nose'],
                       'mouth_left': keypoints['mouth_left'],
                       'mouth_right': keypoints['mouth_right'],
                       'bounding_box': bounding_box}

        coordinates_path = os.path.join(output_folder, f"face_coordinates_{image_file[:-4]}.txt")
        with open(coordinates_path, "w") as file:
            file.write(str(coordinates))

        # 输出结果路径到控制台
        print("Images and coordinates have been saved to folder:", output_folder)
        print(f"Image with keypoints ({image_file}):", image_with_keypoints_path)
        print(f"Face only image ({image_file}):", face_only_path)
        print(f"Face coordinates ({image_file}):", coordinates_path)
    else:
        print("No face detected in", image_file)