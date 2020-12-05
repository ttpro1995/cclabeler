import os 
import json


def mass_rename_jpeg_to_jpg(path):
    img_name_list = os.listdir(path)
    for original_name in img_name_list:
        original_path = os.path.join(path, original_name)
        new_path = original_path.replace("jpeg", "jpg")
        os.rename(original_path, new_path)


def get_all_name(path):
    """

    :param path: "../data/images"
    :return:
    """
    img_list = os.listdir(path)
    img_list_ret = [img.split(".")[-2] for img in img_list]
    return img_list_ret


if __name__ == "__main__":
    # img_list = os.listdir("../data/images")
    path = "../data/images"
    mass_rename_jpeg_to_jpg(path)
    img_list = get_all_name(path)
    print(json.dumps(img_list))