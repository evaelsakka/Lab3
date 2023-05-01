from PIL import Image
import os


class FilteredImage:
    def __init__(self, photo_path):
                while True:
            if not os.path.isfile(photo_path):
                print("Invalid image path.")
                photo_path = input("Enter a valid path of the image file: ")
            else:
                break
        self.image_path = photo_path
        self.img = Image.open(photo_path)

    def apply_filter(self, filter_choice):
                while True:
            if filter_choice not in ["grayscale", "error_diffusion", "sepia", "negative"]:
                print("Invalid filter type.")
                filter_choice = input("Enter one of the following filter types (grayscale, error_diffusion, sepia, negative): ")
            else:
                break

        # Apply the selected filter
        if filter_choice == "grayscale":
            self.img = self.grayscale()
            filter_name = "Grayscale"
        elif filter_choice == "error_diffusion":
            self.img = self.error_diffusion()
            filter_name = "Error_Diffusion"
        elif filter_choice == "sepia":
            self.img = self.sepia()
            filter_name = "Sepia"
        elif filter_choice == "negative":
            self.img = self.negative()
            filter_name = "Negative"
        else:

        # Save the filtered image in the same directory with the same name
        directory = os.path.dirname(self.image_path)
        filename, file_extension = os.path.splitext(os.path.basename(self.image_path))
        new_filename = f"{filename}_{filter_name}{file_extension}"
        new_file_path = os.path.join(directory, new_filename)
        self.img.save(new_file_path)
        print("Filtered image saved under", new_file_path)

    def error_diffusion(self):
        img = self.img.convert("L")
        width, height = img.size
        for y in range(1, height - 1):
            for x in range(1, width - 1):
                old_pixel = img.getpixel((x, y))
                new_pixel = 255 if old_pixel > 128 else 0
                img.putpixel((x, y), new_pixel)
                quant_error = old_pixel - new_pixel
                img.putpixel((x + 1, y), int(img.getpixel((x + 1, y))) + int(7 / 16 * quant_error))
                img.putpixel((x - 1, y + 1), int(img.getpixel((x - 1, y + 1))) + int(3 / 16 * quant_error))
                img.putpixel((x, y + 1), int(img.getpixel((x, y + 1))) + int(5 / 16 * quant_error))
                img.putpixel((x + 1, y + 1), int(img.getpixel((x + 1, y + 1))) + int(1 / 16 * quant_error))
        return img

    def sepia(self):
        img = self.img.convert("RGB")
        width, height = img.size
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                new_r = int(0.393*r + 0.769*g + 0.189*b)
                new_g = int(0.349*r + 0.686*g + 0.168*b)
                new_b = int(0.272*r + 0.534*g + 0.131*b)
                img.putpixel((x, y), (new_r, new_g, new_b))
        return img

    def negative(self):
        img = self.img.convert("RGB")
        width, height = img.size
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                img.putpixel((x, y), (255-r, 255-g, 255-b))
        return img

    def grayscale(self):
        img = self.img.convert("RGB")
        width, height = img.size
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                avg = (r + g + b) // 3
                img.putpixel((x, y), (avg, avg, avg))
        return img


if __name__ == "__main__":
    image_path = input("Enter the path of the image file: ")
    filtered_image = FilteredImage(image_path)
    filter_type = input("Enter a valid filter type (grayscale, error_diffusion, sepia, negative): ")
    filtered_image.apply_filter(filter_type)
