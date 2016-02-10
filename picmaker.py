from math import sin

def makeline(r,g,b):

  i = 0
  s = ""
  while (i < 500):
    s += " %d %d %d " % (r,g,b)
    r += 6 % 255
    g += 20 % 255
    b += 13 % 255
    if(r>255):
      r = 0
    if(g>255):
      g = 0
    if(b>255):
      b= 0
    i += 1

  s += " \n"

  return s


def create(r, g, b):
  f = open('pic.ppm','w')

  header = "P3 500 500 255\n"
  f.write(header)

  i = 0
  image = ""
  while (i < 500):
    image += makeline(r,g,b)
    r += 6 % 255
    g += 20 % 255
    b += 13 % 255
    if(r>255):
      r = 0
    if(g>255):
      g = 0
    if(b>255):
      b= 0
    i = i+1
  
  f.write(image)

create(50,100,234)