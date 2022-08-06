from PIL import Image, ImageFilter

img = Image.open("D:\Python learning\images\Pokemons\_sun_flower.jpg")

print(img)
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))


filter_img = img.filter(ImageFilter.BLUR)
filter_img.save("D:\Python learning\images\Pokemons\_blur_sun_flower.png")

filter_img2 = img.filter(ImageFilter.SHARPEN)
filter_img2.save("D:\Python learning\images\Pokemons\_sharpen_sun_flower.png")

convert_img = img.convert('L')
convert_img.save("D:\Python learning\images\Pokemons\_grey_sun_flower.png")

# filter_img2.show()

rotate_img = img.rotate(90)
rotate_img.save("D:\Python learning\images\Pokemons\_rotate_sun_flower.png")

resize_img = img.resize((500,100))     # takes values in tuple format
resize_img.save("D:\Python learning\images\Pokemons\_resize_sun_flower.png")

crop_img = img.crop((100, 100, 400, 400))
crop_img.save("D:\Python learning\images\Pokemons\_crop_sun_flower.png")


img2 = Image.open("D:\Python learning\images\Pokemons\_astro.jpg")

print(img2.size)
img2.thumbnail((400, 266))     # photo is not sqeeezed i.e. it maintained its aspect ratio on its own
img2.save("astro.png")
print(img2.size)