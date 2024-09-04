from PIL import Image
file_path = "C:\\Users\\billy\\OneDrive\\Documents\\Python Scripts\\png images"
#Use double slashes to avoid unicode error
image = Image.open(f"{file_path}\\empty_scaffold.png")

image.show()