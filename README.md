# Stego Challenge: Uncover the Hidden Image!

Welcome to the Steganography Challenge! Are you ready to embark on an exciting journey into the world of secret messages and hidden images? This challenge is all about the mysterious art of **steganography**, where we cleverly hide one image inside another!

## What’s Steganography?
Steganography is like a magician’s trick—it’s all about concealing information in plain sight! Unlike encryption, where the focus is on scrambling a message to make it unreadable without a key, steganography takes a more creative approach. It hides the message in such a way that no one even realizes there’s something to uncover. You could think of it as the digital version of writing with invisible ink or hiding a note under a painting.

In the digital world, steganography often involves embedding secret data, like text, audio, or even another image, into ordinary files—images being the most popular choice. The result is something called a *stego image*: an image that looks completely normal to anyone viewing it, yet contains a hidden treasure within. And here’s the cool part: if done correctly, the changes made to the image are so subtle that the human eye can’t detect them. This makes steganography both a fascinating and practical tool for secure communication.

One of the most widely used techniques in image steganography is **Least Significant Bit (LSB) substitution**. Think of each pixel in an image as being made up of numbers representing its colors (red, green, and blue). These numbers are usually stored in binary form, like 11001010. The idea behind LSB is to tweak the smallest part of this binary code—the last bit. Changing the least significant bit has almost no effect on the overall color of the pixel, but it creates room to store hidden data. For example, if the original pixel is 11001010, you could change the last bit to 11001011 to hide a small piece of your message. Multiply this by thousands or millions of pixels, and you can store a surprising amount of data in a single image.

Other techniques go beyond LSB, like using mathematical transformations (such as Discrete Cosine Transform or Wavelet Transform) to embed information in less visible parts of the image. While these methods are more complex, they often make the hidden data harder to detect and extract.

Steganography is more than just a clever trick—it’s an intersection of art, technology, and security. It’s been used throughout history for secret communication, and in the digital age, it’s a powerful tool for watermarking, copyright protection, and even covert messaging. Today, you’ll get to explore this amazing concept and see for yourself how fun and ingenious it can be!

## Getting Started
To get in on the fun, you’ll need a Python environment set up with a couple of helpful libraries: Pillow for image processing and NumPy for handling array operations. If you haven’t done so yet, don’t worry! Just pop open your terminal and install with:
```
pip install Pillow numpy
```
* Pillow: A Python Imaging Library that adds image processing capabilities.
* NumPy: A library for numerical computing in Python, useful for handling arrays.
* 
With your environment ready, you can start exploring the provided images and get ready to extract the hidden treasure!

## Your Mission
Now for the exciting part! Your mission, should you choose to accept it, is to analyze the `chall.py` code, figure out how to extract the hidden image and reverse the process! 

Imagine what could be hiding in that stego image! Maybe it’s a hidden message or a delightful illustration waiting to be revealed. The possibilities are endless!
