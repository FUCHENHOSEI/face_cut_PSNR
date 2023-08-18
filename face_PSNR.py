# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os

# 读取文件夹中的图片
folder_path = "face_PSNR_test"
image_files = os.listdir(folder_path)

# 存储 PSNR 结果的列表
psnr_results = []

# 循环计算 PSNR
for i in range(len(image_files)):
    for j in range(i + 1, len(image_files)):
        # 读取图片并将其转换为 RGB 格式
        image_path1 = os.path.join(folder_path, image_files[i])
        image_path2 = os.path.join(folder_path, image_files[j])
        image1 = cv2.cvtColor(cv2.imread(image_path1), cv2.COLOR_BGR2RGB)
        image2 = cv2.cvtColor(cv2.imread(image_path2), cv2.COLOR_BGR2RGB)

        # 调整图像尺寸为相同尺寸
        image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

        # 计算 PSNR
        mse = np.mean((image1 - image2) ** 2)
        psnr = 10 * np.log10((255 ** 2) / mse)
        psnr_results.append((image_files[i], image_files[j], psnr))

# 将 PSNR 结果存储到文本文件
psnr_result_file = "face_PSNR.txt"
with open(psnr_result_file, "w") as file:
    for image1, image2, psnr in psnr_results:
        file.write(f"{image1} vs {image2}: {psnr}\n")

# 输出结果到控制台
print("PSNR results have been saved to:", psnr_result_file)