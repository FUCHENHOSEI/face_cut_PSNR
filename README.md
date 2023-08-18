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
![image](https://github.com/FUCHENHOSEI/face_cut_PSNR/blob/main/fu_test/1.jpg)
![image](https://github.com/FUCHENHOSEI/face_cut_PSNR/blob/main/20230818172324/face_only_1.jpg)
![image](https://github.com/FUCHENHOSEI/face_cut_PSNR/blob/main/20230818172324/face_only_12.jpg)
![image](https://github.com/FUCHENHOSEI/face_cut_PSNR/blob/main/20230818172324/face_only_5.jpg)
