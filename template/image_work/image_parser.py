import os
import json
from pathlib import Path
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def resize_images_in_dir():
    LOCAL_PATH = "save/"
    # result = list(Path(LOCAL_PATH).rglob('*.[Jj][Pp][Gg]')) # for jpg
    result = list(Path(LOCAL_PATH).rglob('*.[Jj][Pp][Ee][Gg]')) # for jpeg
    print(result)
    success_list = []
    size = 750, 750
    BASE_SIZE = 750
    ABSOLUTE_SIZE = (122, 122) # Change image to square
    mobile_flag = True
    for each_jpg in result:
        if '/mobile/' in str(each_jpg):
            continue

        img = Image.open(each_jpg)
        width, height = img.size
        if width > height:
            ratio = width / height
            size = (int(BASE_SIZE * ratio), BASE_SIZE)
        else:
            ratio = height / width
            size = (BASE_SIZE, int(BASE_SIZE * ratio))

        size = ABSOLUTE_SIZE
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.thumbnail(size, Image.ANTIALIAS)
        success_list.append(each_jpg)
        if mobile_flag:
            parsed_file_name = str(each_jpg).split('/')
            parsed_file_name.insert(len(parsed_file_name)-1, 'mobile')
            parsed_file_name = '/'.join(parsed_file_name)
        else:
            parsed_file_name = str(each_jpg)
        parsed_file_name = parsed_file_name.lower().replace('.jpg', '.jpeg')
        img.save(parsed_file_name, 'JPEG')
        print(len(success_list))

if __name__ == "__main__":
    # with open('temp.json') as f:
    #     data = json.load(f)
    # replace_image_extension_to_jpeg(data)

    resize_images_in_dir()