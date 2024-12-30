
import pytesseract
from PIL import Image
import os

# تابعی برای تبدیل تصاویر به متن
def convert_images_to_text(image_folder):
    text_results = {}
    
    for image_file in os.listdir(image_folder):
        if image_file.endswith(('png', 'jpg', 'jpeg', 'tiff', 'bmp')):
            image_path = os.path.join(image_folder, image_file)
            text = pytesseract.image_to_string(Image.open(image_path))
            text_results
            results[image_file] = text
    
    return text_results

# تعیین مسیر پوشه حاوی تصاویر
image_folder = 'path/to/image/folder'
results = convert_images_to_text(image_folder)

# ذخیره نتایج در یک فایل متنی
with open('output.txt', 'w') as output_file:
    for image_name, text in results.items():
        output_file.write(f"--- {image_name} ---\n{text}\n\n")



