from PIL import Image, ImageDraw
import argparse


def generate_meme(image_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size


if '__main__' == __name__:
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="File path to the image.")
    ap.add_argument("--top", required=False, help="Top text over the image.")
    ap.add_argument("--bottom", required=False, help="Bottom text over the image.")
    args = vars(ap.parse_args())

    generate_meme(args['image'])