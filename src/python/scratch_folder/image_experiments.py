from PIL import Image, ImageFilter
image = Image.open(r"data\\preset-images\\hard_image.jpg")

image = image.filter(ImageFilter.FIND_EDGES)

# image = image.filter(ImageFilter.FIND_EDGES)

image = image.filter(ImageFilter.MaxFilter)
image = image.filter(ImageFilter.MaxFilter)
image = image.filter(ImageFilter.MaxFilter)
image = image.filter(ImageFilter.MaxFilter)
image = image.filter(ImageFilter.MaxFilter)
image = image.filter(ImageFilter.MaxFilter)

# image = image.filter(ImageFilter.FIND_EDGES)

image.show()