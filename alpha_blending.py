import cv2

# Read image 1
img1 = cv2.imread("/Users/sparshsinghal/Desktop/sorting visualizer/image_processing/images/test.jpg", 1)

# Read image 2
img2 = cv2.imread("/Users/sparshsinghal/Desktop/sorting visualizer/image_processing/images/test4.jpg", 1)

# Blending the images with alpha as 0.4 and beta as (1 - alpha) 0.6.
img = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)

# Showing the resultant image
cv2.imshow('image', img)

# Wait for a key
cv2.waitKey(0)

cv2.destroyAllWindows()