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

# Noise Models
In image processing, noise refers to the random variation of brightness or color information in images and is usually unwanted. Different noise models are used to simulate various types of noise that can affect digital images. Here are general definitions for some common noise models:

# 1. Gaussian Noise (Normal Noise)
Gaussian noise is statistical noise with a probability density function (PDF) equal to that of the normal distribution, also known as the Gaussian distribution. It is characterized by its mean (average value) and standard deviation (spread or variance). Gaussian noise affects each pixel in the image in a way that the overall distribution of the noise follows a Gaussian curve.

# 2. Salt-and-Pepper Noise (Impulse Noise)
Salt-and-pepper noise presents itself as sparsely occurring white and black pixels. This type of noise is also known as impulse noise because the corrupted pixels are either set to the maximum value (salt) or the minimum value (pepper). It typically occurs due to sharp and sudden disturbances in the image signal.

# 3. Uniform Noise
Uniform noise has a constant PDF. It means that every value in the range of possible noise values has an equal probability of occurring. It can be represented as noise uniformly distributed over a particular range.

# Image Addition, Subtraction, Multiplication, Division, and Alpha Blending

- Alpha Blending: A technique in computer graphics where two images are combined by considering their alpha channels (opacity). The resulting image is a blend based on the transparency levels of each pixel.

- Addition: Combining two images by adding the pixel values of the corresponding pixels. This can increase the brightness and contrast of the resulting image.

- Subtraction: Combining two images by subtracting the pixel values of one image from the corresponding pixels of the other. This can be used to highlight differences between images.

- Multiply: Combining two images by multiplying the pixel values of corresponding pixels. This can darken the resulting image and is often used to create shadow effects.

- Division: Combining two images by dividing the pixel values of one image by the corresponding pixels of the other. This can be used for normalization or to highlight areas with similar intensities.

# Color Map:
This script demonstrates a simple image processing workflow using OpenCV and Matplotlib in Python. The script performs the following steps:

Reading the RGB Image: The image is read from the specified file path using OpenCV's cv2.imread function.
Converting to Grayscale: The RGB image is converted to a grayscale image using the cv2.cvtColor function with the cv2.COLOR_BGR2GRAY flag.
Applying a Colormap: A colormap (specifically, the JET colormap) is applied to the grayscale image using the cv2.applyColorMap function. This step enhances the visualization of different intensity levels in the grayscale image.
Displaying Images: The original RGB image and the heatmap image are displayed side by side using Matplotlib. The plt.subplot function is used to create a subplot layout, and the images are displayed without axes for a cleaner presentation.
This script is useful for visualizing intensity variations in grayscale images and can be extended for various image processing applications such as heatmap generation, feature extraction, and more. To run this script, ensure you have OpenCV and Matplotlib installed in your Python environment.

# Pyramid
In image processing, a pyramid is a multi-scale representation of an image. This technique involves creating a series of images, each one a lower resolution (and typically smaller in size) than the previous. Pyramids are useful in various applications such as image compression, image recognition, and computer vision tasks like object detection.
