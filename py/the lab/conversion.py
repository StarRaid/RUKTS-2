
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

def makeCoords(start:tuple,size:tuple) -> tuple:
    return start+(start[0]+size[0],start[1]+size[1])

for i in range (0,10):
	numbers.append(base.crop(makeCoords((250,i*8),(5,7))))
    
for i in range (0,8):
	templates.append(base.crop(makeCoords((0,i*40),(250,40))))
    
templates.reverse()

imgIn=img.open(input("Image: "))
outX=int(input("X count: "))
outY=int(input("Y count: "))
offsetX=int(input("X start: "))
offsetY=int(input("Y start: "))

output = img.new(mode= "RGB", size= (250*outX,40*outY), color=(255,255,255))

#vehLen=int(input("Vehicle sprite length: "))-1

# Set to 0 for Gwyd sprites, 1 for Hana sprites
s=1
sampleSizes=[[(8,24),(21,18),(32,12),(21,18)],[(8,23),(20,16),(33,13),(20,16)]]
sampleCoordsIn=[[(0,0),(10,0),(33,0),(67,0),(90,0),(100,0),(123,0),(157,0)],[(0,0),(10,0),(32,0),(67,0),(89,0),(99,0),(121,0),(156,0)]]
sampleCoordsOut=[[(2,5),(19,5),(48,9),(89,5),(119,5),(136,5),(165,9),(206,5)],[(2,6),(19,7),(48,8),(90,7),(119,6),(136,7),(165,8),(207,7)]]
sampleOffset=[179,178]

for x in range(0,outX):
    for y in range(0,outY):
        
        #Template
        output.paste(templates[7],makeCoords((250*x,40*y),(250,40)))
        
        #X Digits
        output.paste(numbers[getdig(x,1)],makeCoords((250*x+237,40*y+9),(5,7)))
        output.paste(numbers[getdig(x,0)],makeCoords((250*x+243,40*y+9),(5,7)))
        
        #Y Digits
        output.paste(numbers[getdig(y,1)],makeCoords((250*x+237,40*y+28),(5,7)))
        output.paste(numbers[getdig(y,0)],makeCoords((250*x+243,40*y+28),(5,7)))
        
        #Sprite conversion
        for n in range(0,8):
            size=sampleSizes[s][n%4]
            coord=(sampleCoordsIn[s][n][0]+sampleOffset[s]*x+offsetX,sampleCoordsIn[s][n][1]+25*y+offsetY)
            target=makeCoords(coord,size)
            imgTemp=imgIn.crop(target)
            coord=(250*x+sampleCoordsOut[s][n][0],40*y+sampleCoordsOut[s][n][1])
            target=makeCoords((coord[0],coord[1]),size)
            output.paste(imgTemp,target)
            


# Slut

#output.putpalette(paletteImage.getpalette())
output.save("output.png")

