from PIL import Image

# ASCII characters from darkest to lightest
ASCII_CHARS = "@%#*+=-:. "

# Resize image maintaining aspect ratio
def resize_image(image, new_width=60):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.5)
    return image.resize((new_width, new_height))

# Convert image to grayscale
def grayify(image):
    return image.convert("L")

# Convert pixels to ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

def convert_to_ascii(image_path, output_file='ascii_output.txt', width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print("Error loading image:", e)
        return None

    image = resize_image(image, new_width=width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    pixel_count = len(ascii_str)
    ascii_image = "\n".join([ascii_str[index:(index + width)] for index in range(0, pixel_count, width)])

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(ascii_image)
        print(f"ASCII art written to {output_file}")
    except Exception as e:
        print("Error saving ASCII art:", e)

    return ascii_image

# Run conversion
ascii_image = convert_to_ascii("D:/AD/portifilo/image/git_logo.png", width=50)
if ascii_image:
    print(ascii_image)



'''from PIL import Image

# ASCII characters used to represent pixel brightness
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # Adjust for terminal aspect ratio
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")  # Convert to grayscale

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''.join(ASCII_CHARS[pixel // 25] for pixel in pixels)
    return ascii_str

def image_to_ascii(path, new_width=100):
    try:
        image = Image.open(path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)
    img_width = image.width

    ascii_img = ""
    for i in range(0, len(ascii_str), img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"

    return ascii_img

# ✅ Use the full path to avoid file-not-found issues
ascii_image = image_to_ascii("D:/AD/portifilo/image/git_logo.png", new_width=60)

if ascii_image:
    with open("ascii_output.txt", "w") as f:
        f.write(ascii_image)
    print(ascii_image)
else:
    print("Image conversion failed. Make sure the file name and path are correct.")
'''