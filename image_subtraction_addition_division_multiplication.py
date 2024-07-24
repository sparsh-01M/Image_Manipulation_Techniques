# subtraction
from PIL import Image
image1 = Image.open('images/test2.jpg')
image2 = Image.open('images/test.jpg')
image_new = Image.new("RGB", image1.size)
pixel_map_new = image_new.load()
# if image1.size != image2.size:
#     raise ValueError("Images must be the same size")
pixel_map = image1.load() 
width, height = image1.size
for i in range(width):
    for j in range(height):
        x1, y1, z1 = image1.getpixel((i, j))
        x2, y2, z2 = image2.getpixel((i, j))
        grayscale =  ((x1-x2) + (y1 - y2) + (z1 - z2))
        # grayscale = grayscale//3
        pixel_map_new[i, j] = (int(grayscale), int(grayscale), int(grayscale)) 

image_new.save("grayscale", format='png') 
image_new.show()

# Division
from PIL import Image
image = Image.open('test.jpg')
pixel_map = image.load() 
width, height = image.size
for i in range(width):
    for j in range(height):
        x, y, z = image.getpixel((i, j))
        grayscale =  ((x//3) + (y//3) + (z//3))
        grayscale = grayscale//3
        pixel_map[i, j] = (int(grayscale), int(grayscale), int(grayscale))
image.save("grayscale", format = 'png')
image.show()

# Addition
from PIL import Image
image1 = Image.open('images/test2.jpg')
image2 = Image.open('images/test.jpg')
image_new = Image.new("RGB", image1.size)
pixel_map_new = image_new.load()
# if image1.size != image2.size:
#     raise ValueError("Images must be the same size")
pixel_map = image1.load() 
width, height = image1.size
for i in range(width):
    for j in range(height):
        x1, y1, z1 = image1.getpixel((i, j))
        x2, y2, z2 = image2.getpixel((i, j))
        grayscale =  ((x1 + x2) + (y1 + y2) + (z1 + z2))
        # grayscale = grayscale//3
        pixel_map_new[i, j] = (int(grayscale), int(grayscale), int(grayscale)) 

image_new.save("grayscale", format='png') 
image_new.show()

# Multiplication
from PIL import Image
image1 = Image.open('images/test2.jpg')
image2 = Image.open('images/test.jpg')
image_new = Image.new("RGB", image1.size)
pixel_map_new = image_new.load()

# Value error can be raised if images are of different size or they can be treated as shown below.
# if image1.size != image2.size:
#     raise ValueError("Images must be the same size")

pixel_map = image1.load() 
width, height = image1.size
for i in range(width):
    for j in range(height):
        x1, y1, z1 = image1.getpixel((i, j))
        x2, y2, z2 = image2.getpixel((i, j))
        # multiplying pixel values of two different images
        # grayscale = ((x1 * x2) + (y1 * y2) + (z1 * z2))
        # multiplying by constant
        k = 5 # can be any number
        grayscale = ((x1 * k) + (y1 * k) + (z1 * k))
      
        grayscale = grayscale//3        # normalization
        pixel_map_new[i, j] = (int(grayscale), int(grayscale), int(grayscale)) 

image_new.save("grayscale", format='png') 
image_new.show()
