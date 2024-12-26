from PIL import Image
import numpy as np

# Load the images
cover_image = Image.open('img.jpg')
hidden_image = Image.open('rt.jpg')

# Ensure both images are the same size
hidden_image = hidden_image.resize(cover_image.size)

# Convert images to numpy arrays
cover_data = np.array(cover_image)
hidden_data = np.array(hidden_image)

# Embed the hidden image into the cover image
# Keep the 7 most significant bits of the cover image and add the 1 most significant bits of the hidden image
stego_data = (cover_data & 0b11111110) | (hidden_data >> 7)

# Create and save the new image
stego_image = Image.fromarray(stego_data.astype('uint8'))
stego_image.save('stego.png')