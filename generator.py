from PIL import Image, ImageDraw, ImageFont
import argparse


def generate_meme(image_path, font_path='./res/fonts/impact.ttf', font_size=9):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size

    font = ImageFont.truetype(font=font_path, size=int(image_height * font_size) // 100)

if '__main__' == __name__:
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="File path to the image.")
    ap.add_argument("--top", required=False, help="Top text over the image.")
    ap.add_argument("--bottom", required=False, help="Bottom text over the image.")
    args = vars(ap.parse_args())

    generate_meme(args['image'])