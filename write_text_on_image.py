from PIL import Image, ImageFont, ImageDraw

img = Image.open('hilltop.jpg')

font = ImageFont.truetype("arial.ttf", 30)

text = "Welcome to Hilltop"

edited = ImageDraw.Draw(img)

edited.text((300, 300), text, (0, 0, 0), font=font)

img.save('final.jpg')