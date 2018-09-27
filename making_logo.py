# from PIL import Image, ImageDraw, ImageFont
from wand.image import Image as WI
# import wand
import image
import random


wm_path = 'C:/Users/gili/Documents/image_processing_workshop/watermark/modified_logos/mod_cr3.png'
#origin_path = '/home/user/PycharmProjects/workshop/val/{0}.jpg'
clean_path = 'C:/Users/gili/Documents/image_processing_workshop/watermark/clean/{0}.jpg'
img_with_wm_path = 'C:/Users/gili/Documents/image_processing_workshop/watermark/gili/rand/{0}.jpg'

# help method to resize the original logo
def resize(img):
    size = (32, 32)
    im = Image.open(img.format(''))
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(img.format('mod_'), "JPEG")


def crop(j, path):
    img = Image.open(origin_path.format(j))
    area = (0, 0, 256, 256)
    cropped_img = img.crop(area)
    cropped_img.save(path.format(j), "JPEG")


def main():
    # resize(wm_path)
    p = 0
    for j in range(0,30):
        x, y = random.randint(0,224), random.randint(0,224)
        
        for i in range(1, 100):
            # crop(i, clean_path)
            # random coordinates of the logo
            #x, y = random.randint(0,224), random.randint(0, 224)
            
            with WI(filename=clean_path.format(i)) as background:
                with WI(filename=wm_path) as watermark:
                    # place the watermark on the background with transparency 0.5 positioned x,y
                    background.watermark(watermark, 0.5, x, y)
                background.save(filename=img_with_wm_path.format(p))
                p = p + 1


if __name__ == "__main__":
    main()
