from PIL import Image

#read the image
im = Image.open("image.jpg")

#image size
size=(64,64)

#resize image
out = im.resize(size)

#save resized image
out.save('resize-image.jpg')