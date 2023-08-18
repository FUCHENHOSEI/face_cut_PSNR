# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os

# ��ȡ�ļ����е�ͼƬ
folder_path = "face_PSNR_test"
image_files = os.listdir(folder_path)

# �洢 PSNR ������б�
psnr_results = []

# ѭ������ PSNR
for i in range(len(image_files)):
    for j in range(i + 1, len(image_files)):
        # ��ȡͼƬ������ת��Ϊ RGB ��ʽ
        image_path1 = os.path.join(folder_path, image_files[i])
        image_path2 = os.path.join(folder_path, image_files[j])
        image1 = cv2.cvtColor(cv2.imread(image_path1), cv2.COLOR_BGR2RGB)
        image2 = cv2.cvtColor(cv2.imread(image_path2), cv2.COLOR_BGR2RGB)

        # ����ͼ��ߴ�Ϊ��ͬ�ߴ�
        image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

        # ���� PSNR
        mse = np.mean((image1 - image2) ** 2)
        psnr = 10 * np.log10((255 ** 2) / mse)
        psnr_results.append((image_files[i], image_files[j], psnr))

# �� PSNR ����洢���ı��ļ�
psnr_result_file = "face_PSNR.txt"
with open(psnr_result_file, "w") as file:
    for image1, image2, psnr in psnr_results:
        file.write(f"{image1} vs {image2}: {psnr}\n")

# ������������̨
print("PSNR results have been saved to:", psnr_result_file)