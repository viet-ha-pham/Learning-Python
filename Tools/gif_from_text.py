from PIL import Image, ImageDraw, ImageFont
import os

def create_text_gif(text, output_path, font_path=None, image_size=(500, 500), font_size=90, duration=300):
    """
    Creates an animated GIF that displays each word of the input text sequentially.

    Parameters:
        text (str): The input text to animate.
        output_path (str): The output file path for the GIF.
        font_path (str): Path to the .ttf font file. Defaults to system default.
        image_size (tuple): Size of the GIF image (width, height).
        font_size (int): Font size for the text.
        duration (int): Duration (in milliseconds) each frame is displayed.
    """
    # Split the text into words
    words = text.split()

    # Create a list to hold frames
    frames = []

    # Set up the font
    if font_path is None:
        font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(font_path, font_size)

    # Create frames for each word
    for word in words:
        # Create a blank image with white background
        img = Image.new('RGB', image_size, color='white')
        draw = ImageDraw.Draw(img)

        # Get text size to center it
        text_bbox = draw.textbbox((0, 0), word, font=font)  # Get bounding box of the text
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = (image_size[0] - text_width) // 2
        text_y = (image_size[1] - text_height) // 2

        # Draw the word on the image
        draw.text((text_x, text_y), word, fill='black', font=font)

        # Append the frame to the list
        frames.append(img)

    # Save the frames as an animated GIF
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0
    )

# Example usage
if __name__ == "__main__":
    input_text = "Happy New Year"
    output_gif_path = "happy new year.gif"

    font_path = "fonts/Roboto-VariableFont_wdth,wght.ttf"

    create_text_gif(input_text.upper(), output_gif_path, font_path)
    print(f"GIF saved to {output_gif_path}")
