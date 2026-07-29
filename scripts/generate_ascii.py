from PIL import Image

def image_to_ascii(image_path, output_path, width=80):
    """Convert an image to ASCII art."""
    try:
        img = Image.open(image_path)
        
        # Resize image
        aspect_ratio = img.height / img.width
        new_height = int(width * aspect_ratio * 0.55)
        img = img.resize((width, new_height))
        
        # Convert to grayscale
        img = img.convert('L')
        
        # ASCII characters (dark to light)
        ascii_chars = "@%#*+=-:. "
        
        # Convert pixels to ASCII
        ascii_art = ""
        for y in range(img.height):
            for x in range(img.width):
                pixel = img.getpixel((x, y))
                ascii_index = int(pixel / 255 * (len(ascii_chars) - 1))
                ascii_art += ascii_chars[ascii_index]
            ascii_art += "\n"
        
        # Save to file
        with open(output_path, 'w') as f:
            f.write(ascii_art)
        
        print(f"ASCII art saved to {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_to_ascii("assets/profile.png", "assets/profile-ascii.txt")
