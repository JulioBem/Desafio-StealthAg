#Importações
from PIL import Image
from collections import Counter
import prettytable

#Load da imagem e conversão para jpg
img = Image.open("img/meteor_challenge_01.png")
img.load()
new_img = Image.new("RGB", img.size, (255, 255, 255))
new_img.paste(img, mask=img.split()[3])
size = w, h = new_img.size
data = new_img.load()

#Variáveis
colors = []
water = 0

#Procura a cor
for x in range (w):
    for y in range (h):
        color = data[x,y]
        hex_color = '#'+''.join([hex (c)[2:].rjust(2, '0') for c in color ])
        colors.append(hex_color)
        if hex_color == "#ff0000": #caso seja encontrado a cor do meteoro, verá se logo abaixo há água
            for y in range (h):
                color = data [x,y]
                hex_color = '#'+''.join([hex (c)[2:].rjust(2, '0') for c in color ])
                if hex_color == "#0000ff":
                    water += 1
                    break

#Display do output
pt = prettytable.PrettyTable(["Color", "Count"])

for color, count in Counter(colors).items():
    if (color == "#ffffff"):
        color = 'Number of Stars'
        pt.add_row([color, count])
    if (color == "#ff0000"):
        color = 'Number of Meteors'
        pt.add_row([color, count])

pt.add_row(['Meteors Falling on the Water', water])

print(pt)