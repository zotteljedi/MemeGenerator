from PIL import Image, ImageDraw, ImageFont
import textwrap
import argparse


def generate_meme(image_path, top_text, bottom_text, font_path='./res/fonts/impact.ttf', font_size=9):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size

    font = ImageFont.truetype(font=font_path, size=int(image_height * font_size) // 100)

    top_text = top_text.upper()
    bottom_text = bottom_text.upper()

    char_width, char_height = font.getsize('A')
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(top_text, width=chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)

    y = 10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='white', font=font)
        y += line_height

if '__main__' == __name__:
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="File path to the image.")
    ap.add_argument("--top", default='', required=False, help="Top text over the image.")
    ap.add_argument("--bottom", default='', required=False, help="Bottom text over the image.")
    args = vars(ap.parse_args())

    generate_meme(args['image'], args['top'], args['bottom'])