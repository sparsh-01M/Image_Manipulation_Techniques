import cv2
import matplotlib.pyplot as plt

# Step 1: Read the RGB image
image = cv2.imread('image_processing/images/test.jpg')

# Step 2: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply a colormap to the grayscale image
heatmap = cv2.applyColorMap(gray_image, cv2.COLORMAP_JET)

# Step 4: Display the original and heatmap images using Matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Heatmap Image')
plt.imshow(cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
