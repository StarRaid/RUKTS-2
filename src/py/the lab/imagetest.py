
from PIL import Image as img
import math

base=img.open("../../templates/lengths.png")
#paletteImage=img.open("templates/palette.png")
numbers=[]
templates=[]

def getdig(a,pos:int) -> int:
    try:
        pos+=1
        a=str(math.floor(a))
        return int(a[-pos])
    except:
        return 0

for i in range (0,10):
	numbers.append(base.crop((250,i*8,255,(i*8)+7)))
    
for i in range (0,8):
	templates.append(base.crop((0,i*40,250,(i+1)*40)))
    
templates.reverse()

outX=int(input("Articulated parts: "))
outY=int(input("Livery count: "))
outY+=int(input("Fixture type count: "))

output = img.new(mode= "RGB", size= (250*outX,40*outY), color=(255,255,255))

vehLen=int(input("Vehicle sprite length: "))-1

for x in range(0,outX):
    for y in range(0,outY):
        
        #Template
        coords=(250*x,40*y,250*(x+1),40*(y+1))
        output.paste(templates[vehLen],coords)
        
        #X Digits
        coords=(250*x+237,40*y+9,250*x+242,40*y+16)
        output.paste(numbers[getdig(x,1)],coords)
        coords=(250*x+243,40*y+9,250*x+248,40*y+16)
        output.paste(numbers[getdig(x,0)],coords)
        
        #Y Digits
        coords=(250*x+237,40*y+28,250*x+242,40*y+35)
        output.paste(numbers[getdig(y,1)],coords)
        coords=(250*x+243,40*y+28,250*x+248,40*y+35)
        output.paste(numbers[getdig(y,0)],coords)
        


# Slut

#output.putpalette(paletteImage.getpalette())
output.save("output.png")

