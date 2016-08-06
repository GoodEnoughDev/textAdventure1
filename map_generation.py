import png

f = open('test.png', 'wb')
w = png.Writer(255, 255, greyscale=False)
l = list()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,0,255)

for i in range(255):
    l.append([])
    for i2 in range(255):
        if i2 < 100:
            l[i].append(0)
            l[i].append(0)
            l[i].append(255)
        else:
            l[i].append(255)
            l[i].append(0)
            l[i].append(0)


w.write(f, l)
print([range(256)])
f.close()