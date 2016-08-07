import sys
import png
from noise import pnoise2, snoise2

f = open('test.png', 'wb')
array_size = 512

w = png.Writer(array_size-1, array_size-1, greyscale=False)
l = list()

grey = (128, 128, 128)
green = (0, 255, 0)
blue = (0,0,255)

mountain_threshold = 150
sea_threshold = 100

if len(sys.argv) not in (2, 3, 4, 5) or '--help' in sys.argv or '-h' in sys.argv:
    print('2dtexture.py FILE [OCTAVES]')
    print()
    print(__doc__)
    raise SystemExit

if len(sys.argv) > 2:
    octaves = int(sys.argv[2])
    mountain_threshold = int(sys.argv[4])
    sea_threshold = int(sys.argv[3])
else:
    octaves = 1
freq = 1.0 * octaves


map_array = list()

for y in range(array_size):
    map_array.append([])
    for x in range(array_size):
        map_array[y].append(int((snoise2(x / freq, y / freq, octaves) * 127.0 + 128.0)))

for i in range(array_size-1):
    l.append([])
    for i2 in range(array_size-1):
        if map_array[i][i2] < sea_threshold:
            l[i].extend(blue)
        elif map_array[i][i2] > mountain_threshold:
            l[i].extend(grey)
        else:
            l[i].extend(green)

w.write(f, l)
f.close()