# face_cut_PSNR

This project is a script that can directly calibrate all the faces in multiple images from the input, crop the faces into a new IMAGE, and then compare these images containing just the faces to each other for PSNR.

Implementation of the MTCNN face detector for Keras in Python3.4+. It is written from scratch, using as a reference the implementation of MTCNN from David Sandberg (FaceNet's MTCNN) in Facenet. It is based on the paper Zhang, K et al. (2016) [ZHANG2016].

## Installation

Currently, it is only supported in Python3.4 onwards. It can be installed through pip:
```
pip install mtcnn
```
This implementation requires OpenCV>=4.1 and Keras>=2.0.0 (any Tensorflow supported by Keras will be supported by this MTCNN package). If this is the first time you use tensorflow, you will probably need to install it in your system:
```
pip install tensorflow
```
or with conda,
```
conda install tensorflow
```
Note that tensorflow-gpu version can be used instead if a GPU device is available on the system, which will speed up the results.

## Usage 
### Please first put the required original images in the fu_text folder as follows (you can put as many as you want):
![image](https://github.com/FUCHENHOSEI/face_cut_PSNR/blob/main/fu_test/1.jpg)

### The cropped images will be in a folder named with the current time, where the cropped face images are as follows:
![image](https://github.com/FUCHENHOSEI/face_cut_PSNR/blob/main/20230818172324/face_only_1.jpg)
![image](https://github.com/FUCHENHOSEI/face_cut_PSNR/blob/main/20230818172324/face_only_12.jpg)
![image](https://github.com/FUCHENHOSEI/face_cut_PSNR/blob/main/20230818172324/face_only_5.jpg)

### Then put the face images that need to be compared in the face_PSNR_test folder (this step needs to be manually picked by yourself, you can put any number of sheets, each other directly will be all compared):
```
face_only_1.jpg vs face_only_12.jpg: 29.586873821117315
face_only_1.jpg vs face_only_5.jpg: 30.005418830696943
face_only_12.jpg vs face_only_5.jpg: 31.302872037270483
```
