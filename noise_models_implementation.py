import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_gaussian_noise(image, mean=0, std_dev=25):
    gaussian_noise = np.random.normal(mean, std_dev, image.shape).astype('uint8')
    noisy_image = cv2.add(image, gaussian_noise)
    return noisy_image

def add_erlang_noise(image, shape=2, scale=1):
    erlang_noise = np.random.gamma(shape, scale, image.shape).astype('uint8')
    noisy_image = cv2.add(image, erlang_noise)
    return noisy_image

def add_exponential_noise(image, scale=50):
    exponential_noise = np.random.exponential(scale, image.shape).astype('uint8')
    noisy_image = cv2.add(image, exponential_noise)
    return noisy_image

def add_uniform_noise(image, low=-50, high=50):
    uniform_noise = np.random.uniform(low, high, image.shape).astype('uint8')
    noisy_image = cv2.add(image, uniform_noise)
    return noisy_image

def add_impulse_noise(image, salt_prob=0.05, pepper_prob=0.05):
    noisy_image = image.copy()
    total_pixels = image.size // image.shape[2]
    num_salt = int(total_pixels * salt_prob)
    num_pepper = int(total_pixels * pepper_prob)
    
    # Salt noise
    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1], :] = 255
    
    # Pepper noise
    pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1], :] = 0
    
    return noisy_image

# Load an example image
image = cv2.imread('image_processing/images/test.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Add different noises to the image
gaussian_noisy_image = add_gaussian_noise(image)
erlang_noisy_image = add_erlang_noise(image)
exponential_noisy_image = add_exponential_noise(image)
uniform_noisy_image = add_uniform_noise(image)
impulse_noisy_image = add_impulse_noise(image)

# Display the images
plt.figure(figsize=(15, 10))

plt.subplot(231), plt.title('Original Image')
plt.imshow(image), plt.axis('off')

plt.subplot(232), plt.title('Gaussian Noise')
plt.imshow(gaussian_noisy_image), plt.axis('off')

plt.subplot(233), plt.title('Erlang Noise')
plt.imshow(erlang_noisy_image), plt.axis('off')

plt.subplot(234), plt.title('Exponential Noise')
plt.imshow(exponential_noisy_image), plt.axis('off')

plt.subplot(235), plt.title('Uniform Noise')
plt.imshow(uniform_noisy_image), plt.axis('off')

plt.subplot(236), plt.title('Impulse Noise')
plt.imshow(impulse_noisy_image), plt.axis('off')

plt.show()
