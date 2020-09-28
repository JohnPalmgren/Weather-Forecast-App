from PIL import Image

filen = r'top_icon.webp'
img = Image.open(filen)
img.save('top_icon.ico',format = 'ICO', sizes=[(16,16)])
