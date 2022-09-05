import shutil

from PIL import Image
import os

OUT_DIR = './out'
DATASET_DIR = './dataset'

def create_dir(directory):
    if os.path.exists(directory) and os.path.isdir(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

def crop_photo_and_put_in_folders(coal_path, mask_path, coal_out_path, mask_out_path, counted_images):
    step = 512

    image_counter = counted_images
    coal_img = Image.open(coal_path)
    coal_img = coal_img.convert('RGBA')

    mask_img = Image.open(mask_path)
    mask_img = mask_img.convert('RGBA')
    # img= img.resize((500,500))  # photo resize to this param

    for i in range(0, coal_img.size[1] + 1, step):

        if (i + step) > coal_img.size[1]: break
        for j in range(0, coal_img.size[0] + 1, step):
            if (j + step) > coal_img.size[0]:
                break
            else:
                image_temp = coal_img.crop((j, i, j + step, i + step))
                path_to_save = os.path.join(coal_out_path, 'c' + str(image_counter) + '.png')
                image_temp.save(path_to_save)
                print("saving image: " + path_to_save)
                image_counter += 1

                image_temp_l = image_temp.rotate(-90)
                path_to_save = os.path.join(coal_out_path, 'c' + str(image_counter) + '.png')
                image_temp_l.save(path_to_save)
                print("saving image: " + path_to_save)
                image_counter += 1
                #
                image_temp_r = image_temp.rotate(90)
                path_to_save = os.path.join(coal_out_path, 'c' + str(image_counter) + '.png')
                image_temp_r.save(path_to_save)
                print("saving image: " + path_to_save)
                image_counter += 1

                image_temp_u = image_temp.rotate(180)
                path_to_save = os.path.join(coal_out_path, 'c' + str(image_counter) + '.png')
                image_temp_u.save(path_to_save)
                print("saving image: " + path_to_save)
                image_counter += 1
    image_counter = counted_images
    for i in range(0, mask_img.size[1] + 1, step):

        if (i + step) > mask_img.size[1]: break
        for j in range(0, mask_img.size[0] + 1, step):
            if (j + step) > mask_img.size[0]:
                break
            else:
                image_temp = mask_img.crop((j, i, j + step, i + step))
                path_to_save = os.path.join(mask_out_path, 'm' + str(image_counter) + '.png')
                image_temp.save(path_to_save)
                print("saving image: " + path_to_save)
                image_counter += 1

                image_temp_l = image_temp.rotate(-90)
                path_to_save = os.path.join(mask_out_path, 'm' + str(image_counter) + '.png')
                image_temp_l.save(path_to_save)
                print("saving image: " + path_to_save)
                image_counter += 1
                #
                image_temp_r = image_temp.rotate(90)
                path_to_save = os.path.join(mask_out_path, 'm' + str(image_counter) + '.png')
                image_temp_r.save(path_to_save)
                print("saving image: " + path_to_save)
                image_counter += 1

                image_temp_u = image_temp.rotate(180)
                path_to_save = os.path.join(mask_out_path, 'm' + str(image_counter) + '.png')
                image_temp_u.save(path_to_save)
                print("saving image: " + path_to_save)
                image_counter += 1
    return image_counter

if __name__ == '__main__':
    coal_dir = os.path.join(DATASET_DIR, "coal")
    mask_dir = os.path.join(DATASET_DIR, "mask")

    coal_images = os.listdir(coal_dir)
    mask_images = os.listdir(mask_dir)

    coal_images.sort()
    mask_images.sort()

    coal_out = os.path.join(OUT_DIR, "coal")
    mask_out = os.path.join(OUT_DIR, "mask")

    create_dir(coal_out)
    create_dir(mask_out)
    counted_images = 1

    for i in range(len(coal_images)):
        coal_im = os.path.join(coal_dir, coal_images[i])
        mask_im = os.path.join(mask_dir, mask_images[i])
        counted_images = crop_photo_and_put_in_folders(coal_im, mask_im, coal_out, mask_out, counted_images)
