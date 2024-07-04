from PIL import Image

def encrypt_image(input, output, key):
    img = Image.open(input)
    pixels = img.load()

    width, height = img.size
    #nested loops iterate over each pixel in the image.
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and green
            encrypted_pixel = (g,r,b )

            pixels[i, j] = encrypted_pixel

    img.save(output)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and green
            decrypted_pixel = (g, r, b)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")


input_image = "D:\picture\jewfolder\orignal.jpg"
encrypted_image ="D:\picture\jewfolder\enc_image.jpg"
decrypted_image = "D:\picture\jewfolder\dec_image.jpg"


encrypt_image(input_image, encrypted_image, key=None)
decrypt_image(encrypted_image, decrypted_image, key=None)

