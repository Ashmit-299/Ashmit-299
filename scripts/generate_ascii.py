from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

WIDTH = 70

ASCII_CHARS = "@%#*+=-:. "

BASE_DIR = Path(__file__).resolve().parent.parent

IMAGE_PATH = BASE_DIR / "assets" / "profile.png"
OUTPUT_PATH = BASE_DIR / "assets" / "profile-ascii.txt"


def preprocess(image):

    image = image.convert("L")

    image = ImageOps.autocontrast(image)

    image = ImageEnhance.Contrast(image).enhance(2.2)

    image = image.filter(ImageFilter.SHARPEN)

    return image


def resize(image):

    w, h = image.size

    ratio = h / w

    height = int(WIDTH * ratio * 0.50)

    return image.resize((WIDTH, height))


def convert(image):

    pixels = image.load()

    output = []

    for y in range(image.height):

        line = ""

        for x in range(image.width):

            pixel = pixels[x, y]

            index = int(pixel / 255 * (len(ASCII_CHARS) - 1))

            line += ASCII_CHARS[index]

        output.append(line)

    return "\n".join(output)


def main():

    image = Image.open(IMAGE_PATH)

    image = preprocess(image)

    image = resize(image)

    ascii_art = convert(image)

    OUTPUT_PATH.write_text(ascii_art, encoding="utf-8")

    print(ascii_art)


if __name__ == "__main__":
    main()