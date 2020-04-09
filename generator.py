import argparse


if '__main__' == __name__:
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="File path to the image.")
    ap.add_argument("--top", required=False, help="Top text over the image.")
    ap.add_argument("--bottom", required=False, help="Bottom text over the image.")
    args = vars(ap.parse_args())