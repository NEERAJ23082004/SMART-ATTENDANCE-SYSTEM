#Generate your base64string 
import base64

with open("YOUR_IMAGE.jpg", "rb") as img_file:
    base64string = base64.b64encode(img_file.read()).decode("utf-8")
print(base64string):

