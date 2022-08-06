import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder) # to check if above func works 

print(os.path.exists(output_folder)) # to check if our output folder exist

if not os.path.exists(output_folder):
	os.makedirs(output_folder)

print(os.path.exists(output_folder)) # to check if our output folder exist

for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)
	print(clean_name)
	clean_name = os.path.splitext(filename)[0]
	print(clean_name)
	img.save(f'{output_folder}{clean_name}.png')
	print("Convert done!")