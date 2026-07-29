from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps

BASE_DIR = Path(__file__).resolve().parent.parent

IMAGE_PATH = BASE_DIR / "assets" / "profile.png"
OUTPUT_PATH = BASE_DIR / "assets" / "profile-ascii.txt"

ASCII = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

WIDTH = 58


def resize(image):
    width, height = image.size
    ratio = height / width
    new_height = int(WIDTH * ratio * 0.52)
    return image.resize((WIDTH, new_height))


def preprocess(image):

    image = image.convert("L")

    image = ImageOps.autocontrast(image)

    image = ImageEnhance.Contrast(image).enhance(2.5)

    image = ImageEnhance.Sharpness(image).enhance(2)

    return image


def pixel_to_char(pixel):

    index = pixel * (len(ASCII) - 1) // 255

    return ASCII[index]


def convert(image):

    pixels = image.load()

    lines = []

    for y in range(image.height):

        row = ""

        for x in range(image.width):

            row += pixel_to_char(pixels[x, y])

        lines.append(row.rstrip())

    return lines


def trim(lines):

    while lines and lines[0].strip() == "":
        lines.pop(0)

    while lines and lines[-1].strip() == "":
        lines.pop()

    return lines


def center(lines):

    width = max(len(x) for x in lines)

    centered = []

    for line in lines:

        centered.append(line.center(width))

    return centered


def save(lines):

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main():

    image = Image.open(IMAGE_PATH)

    image = resize(image)

    image = preprocess(image)

    lines = convert(image)

    lines = trim(lines)

    lines = center(lines)

    save(lines)

    print("ASCII generated successfully.")


if __name__ == "__main__":

    main()