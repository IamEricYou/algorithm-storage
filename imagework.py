import os
import json
from pathlib import Path
from PIL import Image

import cv2

def parse_ara_v2_image_extension_to_jpeg(iamge_file):
	parsed_file_name = iamge_file
	if 'travel-content/ara-v2/' in parsed_file_name:
		if '.jpg' in parsed_file_name:
			parsed_file_name = parsed_file_name.replace('.jpg', '.jpeg')

		if '.png' in parsed_file_name:
			parsed_file_name = parsed_file_name.replace('.png', '.jpeg')

	return parsed_file_name



def resize_images_in_dir_edited():
	LOCAL_PATH = "."
	result = list(Path(LOCAL_PATH).rglob('*.[Jj][Pp][Gg]'))  # for jpg
	print(result[0])
	src = cv2.imread('dealpage1.jpg', cv2.IMREAD_COLOR)
	height, width = src.shape[:2]

	# dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
	dst2 = cv2.resize(src, dsize=(600, int(600 * height/width)), interpolation=cv2.INTER_LINEAR)

	# cv2.imshow("src", src)
	# cv2.imshow("dst", dst)
	# cv2.imshow("dst2", dst2)
	cv2.imwrite("IMAGE_NAME.jpg", dst2)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()


def resize_images_in_dir():
	LOCAL_PATH = "."
	result = list(Path(LOCAL_PATH).rglob('*.[Jj][Pp][Gg]'))  # for jpg
	# result = list(Path(LOCAL_PATH).rglob('*.[Pp][Nn][Gg]'))  # for png
	# result = list(Path(LOCAL_PATH).rglob('*.[Jj][Pp][Ee][Gg]')) # for jpeg
	# print(result)
	# return
	success_list = []
	fail_list = []
	size = 122, 122
	BASE_SIZE = 600, 600
	ABSOLUTE_SIZE = 330, 330  # Change image to square
	mobile_flag = True
	for each_jpg in result:
		# try:
		img = Image.open(each_jpg)
		width, height = img.size
		# if width > height:
		# 	ratio = width / height
		# 	size = (int(BASE_SIZE * ratio), BASE_SIZE)
		# else:
		# 	ratio = height / width
		# 	size = (BASE_SIZE, int(BASE_SIZE * ratio))

		# if img.mode in ("RGBA", "P", "LA"):
		# 	img = img.convert("RGB")

		print(Image.ANTIALIAS)
		img.thumbnail(BASE_SIZE, Image.ANTIALIAS)
		success_list.append(each_jpg)
		parsed_file_name = "parsed" + str(each_jpg)
		# parsed_main_name = parsed_main_name.lower().replace('.jpg', '.jpeg')
		# parsed_file_name = parsed_file_name.lower().replace('.jpg', '.jpeg')
		# parsed_main_name = parsed_main_name.lower().replace('.png', '.jpeg')
		# parsed_file_name = parsed_file_name.lower().replace('.png', '.jpeg')
		img.save(parsed_file_name, quality=100, subsampling=0, optimize=True)
		print(parsed_file_name)
		# except:
		# 	fail_list.append(each_jpg)
		
	print(fail_list)

def myprint(d):
	for k, v in d.items():
		if isinstance(v, dict):
			myprint(v)
		else:
			print("{0} : {1}".format(k, v))

if __name__ == "__main__":
	# with open('temp.json') as f:
	#     data = json.load(f)
	# replace_image_extension_to_jpeg(data)

	resize_images_in_dir()
	# resize_images_in_dir_edited()