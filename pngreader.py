from PIL import Image
import os
import sys



def rgb_text(r, g, b, text):
    """Цвет текста по RGB (0-255)"""
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


os.system("clear")

img = Image.open(sys.argv[1])

width, height = img.size

ratio = height/width

rows, columns = os.popen('stty size', 'r').read().split()

size_x = columns
size = (int(columns),round(int(rows)*ratio) if round(int(columns)*ratio) < int(rows) else int(rows)-1)

img = img.convert('RGB')
img = img.resize(size)


width, height = img.size

pixel_char = "▓"

for y in range(height):
    buffer_line = ""
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        buffer_line += rgb_text(r,g,b,pixel_char)
        
    print(buffer_line)
    


