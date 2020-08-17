from PIL import Image

filen = r'30.png'
img = Image.open(filen)
img.save('30.ico',format = 'ICO', sizes=[(120,60)])
