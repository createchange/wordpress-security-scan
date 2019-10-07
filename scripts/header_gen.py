from PIL import Image, ImageFont, ImageDraw
import subprocess

'''
Change ShowText field and end path for expected results
'''

ShowText = 'Non-Web Maintenance'

font = ImageFont.truetype('/usr/share/fonts/DejaVuSans.ttf', 13) #load the font
size = font.getsize(ShowText)  #calc the size of text in pixels
image = Image.new('1', size, 1)  #create a b/w image
draw = ImageDraw.Draw(image)
draw.text((0, 0), ShowText, font=font) #render the text to the bitmap

def mapBitToChar(im, col, row):
    if im.getpixel((col, row)): return ' '
    else: return '#'

for r in range(size[1]):
    print ''.join([mapBitToChar(image, c, r) for c in range(size[0])])
            
        

subprocess.check_output('python header_gen.py > ../headers/non_web_maintenance_header.txt', shell=True)

