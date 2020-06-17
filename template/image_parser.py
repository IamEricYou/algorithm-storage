import os
import json
from pathlib import Path
from PIL import Image

def parse_ara_v2_image_extension_to_jpeg(iamge_file):
    parsed_file_name = iamge_file
    if 'travel-content/ara-v2/' in parsed_file_name:
        if '.jpg' in parsed_file_name:
            parsed_file_name = parsed_file_name.replace('.jpg', '.jpeg')

        if '.png' in parsed_file_name:
            parsed_file_name = parsed_file_name.replace('.png', '.jpeg')

    return parsed_file_name

def resize_images_in_dir(directory):
    # directory = '/workspace/algorithm-storage/template'
    
    result = list(Path(".").rglob("*.[j][p][g]"))
    # print(os.listdir(os.getcwd()))
    # print(result[1])
    # print(len(result))
    wrong_file_list = []
    result = ['tokyo/city_currency_exchange_4.png']
    for each_jpg in result:
        print(each_jpg)
        # try:
        img = Image.open(each_jpg)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        new_file_name = str(each_jpg).replace('.png', '.jpeg')
        img.save(new_file_name, 'JPEG')

        # except:
        #     wrong_file_list.append(each_jpg)

    print(wrong_file_list)
    return

def myprint(d):
    for k, v in d.items():
        if isinstance(v, dict):
            myprint(v)
        else:
            print("{0} : {1}".format(k, v))

def parse_ara_v2_image_extension_to_jpeg(iamge_file):
    parsed_file_name = iamge_file
    if 'travel-content/ara-v2/' in parsed_file_name:
        if '.jpg' in parsed_file_name:
            parsed_file_name = parsed_file_name.replace('.jpg', '.jpeg')

        if '.JPG' in parsed_file_name:
            parsed_file_name = parsed_file_name.replace('.JPG', '.jpeg')

        if '.png' in parsed_file_name:
            parsed_file_name = parsed_file_name.replace('.png', '.jpeg')

        if '.PNG' in parsed_file_name:
            parsed_file_name = parsed_file_name.replace('.PNG', '.jpeg')

    return parsed_file_name

def replace_image_extension_to_jpeg():
    city_objs = CityGuideData.objects.all()
    for city_obj in city_objs:
        if not city_obj.data_sections:
            continue
        obj_list = city_obj.data_sections
        for obj in obj_list:
            parsed_main_img = parse_ara_v2_image_extension_to_jpeg(obj.get('images').get('main'))
            parsed_background_img = []
            if obj.get('images').get('backgrounds'):
                for each_img in obj.get('images').get('backgrounds'):
                    parsed_background_img.append(parse_ara_v2_image_extension_to_jpeg(each_img))

            image_template = {
                'images': {
                    'main': parsed_main_img,
                    'backgrounds': parsed_background_img,
                }
            }
            obj.update(image_template)
            for each_section in obj.get('sub_sections'):
                main_image = each_section.get('images').get('main')
                main_image = parse_ara_v2_image_extension_to_jpeg(main_image)
                mobile_image_list = []
                mobile_image = each_section.get('images').get('mobile')
                for mi in mobile_image:
                    mobile_image_list.append(parse_ara_v2_image_extension_to_jpeg(mi))
                background_image_list = []
                background_image = each_section.get('images').get('backgrounds')
                for bi in background_image:
                    background_image_list.append(parse_ara_v2_image_extension_to_jpeg(bi))
                sub_section_dict = {
                    'images': {
                        'main': main_image,
                        'mobile': mobile_image_list,
                        'backgrounds': background_image_list
                    }
                }
                each_section.update(sub_section_dict)
                if each_section.get('related_places'):
                    for each_related_place in each_section.get('related_places'):
                        main_image_rp = each_related_place.get('images').get('main')
                        main_image_rp = parse_ara_v2_image_extension_to_jpeg(main_image_rp)
                        mobile_image_list_rp = []
                        mobile_image_rp = each_related_place.get('images').get('mobile')
                        if mobile_image_rp:
                            for mi_rp in mobile_image_rp:
                                mobile_image_list_rp.append(parse_ara_v2_image_extension_to_jpeg(mi_rp))
                        background_image_list_rp = []
                        background_image_rp = each_related_place.get('images').get('backgrounds')
                        if background_image_rp:
                            for bi_rp in background_image_rp:
                                background_image_list_rp.append(parse_ara_v2_image_extension_to_jpeg(bi_rp))
                        sub_section_dict_rp = {
                            'images': {
                                'main': main_image_rp,
                                'mobile': mobile_image_list_rp,
                                'backgrounds': background_image_list_rp
                            }
                        }
                        if not mobile_image_list_rp:
                            del sub_section_dict_rp['images']['mobile']
                        each_related_place.update(sub_section_dict_rp)
            city_obj.data_sections = obj_list
            print(city_obj.id)
            # city_obj.save()
            
if __name__ == "__main__":
    # with open('temp.json') as f:
    #     data = json.load(f)
    # replace_image_extension_to_jpeg(data)

    resize_images_in_dir('1')