from PIL import Image, ImageFont, ImageDraw
import os

class ImageEditor:
    def __init__(self, image_path):
        self.file_path = image_path
        self.image = Image.open(image_path)
        
    def rotate(self, degree):
        self.image = self.image.rotate(degree)
        
        #method chanining
        return self
    
    def add_text(self, x, y, text, color=None):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("arial.ttf", 40)
        
        draw.text((x, y), text, font=font, fill=color) 
        return self
    
    def create_thumbnail(self, width, height):
        #splitting file path to be able to save new version
        file, ext = os.path.splitext(self.file_path)
        thumbnail_path = file + ".thumbnail" + ext
        
        self.image.thumbnail((width, height))
        self.image.save(thumbnail_path, "JPEG")
        return self
        
    def save_changes(self, file_add):
        file, ext = os.path.splitext(self.file_path)
        new_path = file + file_add + ext
        self.image.save(new_path, "JPEG")
        return self
        
    def show(self):
        self.image.show()
        
        
image_1 = ImageEditor("C:\\Users\\billy\\OneDrive\\Documents\\Python Scripts\\crosseyedkitten.jpg")
image_1.rotate(180).save_changes("edited")
image_1.add_text(100, 100, "MeOW!", "purple").save_changes("_meow")


