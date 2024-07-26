# Image_Manipulation_Techniques

In this repository we will apply various image processing operations, and try to alter the image in multiple ways.

# Edge-detection:
- Edge detection includes a variety of mathematical methods that aim at identifying edges, defined as curves in a digital image at which the image brightness changes sharply or, more formally, has discontinuities. The same problem of finding discontinuities in one-dimensional signals is known as step detection and the problem of finding signal discontinuities over time is known as change detection. Edge detection is a fundamental tool in image processing, machine vision and computer vision, particularly in the areas of feature detection and feature extraction.[1]

# Canny Edge Detection:
- Canny Edge Detection is a popular edge detection algorithm. It was developed by John F. Canny in
- It is a multi-stage algorithm and we will go through each stages.
- Noise Reduction
- Since edge detection is susceptible to noise in the image, first step is to remove the noise in the image with a 5x5 Gaussian filter. We have already seen this in previous chapters.
- Finding Intensity Gradient of the Image
- Smoothened image is then filtered with a Sobel kernel in both horizontal and vertical direction to get first derivative in horizontal direction (Gx) and vertical direction (Gy). From these two images, we can find edge gradient and direction for each pixel as follows:

 

