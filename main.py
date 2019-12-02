# code by TFC(James Packham)
# 28-11-2019
#

from tkinter import *
from math import sqrt
import time


global resolution
global size  # i know i really shouldn't use global but im lazy
resolution = 160000  # how many rectangels in the whole thing
size = 1000  # size of the canvas, changing these does however break it a tad as i never got round to adding it in
MAX_ITERATIONS = 100


def color_map(iterations):
    # Maps the number of iterations to a hex (#RRGGBB) color
    brightness = int(((iterations - MAX_ITERATIONS) / (0 - MAX_ITERATIONS)) * 255)
    return "#{0:02x}{0:02x}{0:02x}".format(brightness)

resolution = (sqrt(resolution))/1000

# this bit shows the pos of the curser
def motion(event):
    global view
    # global resolution
    x, y = event.x, event.y
    a, b = (resolution*x)-((resolution*size)-(resolution*size*0.75)), (resolution*y)-((0.4*size)-(resolution*size*0.5))
    print('{}, {}'.format(int(a), int(b)))


def check(r, f):
    z = 0+0j
    loops = 0
    # this loop iterated the code untill it either gets to big or we hit MAX_ITERATIONS loops
    while (z.real*z.real) + (z.imag*z.imag) <= 4 and loops < MAX_ITERATIONS:
        z = (z*z) + complex(r/100, f/100)
        loops += 1

    return loops


pixel = 1  # the size of each pixel


def fractal():
    # this loop goes thru each pixel which correlates to a pos on the complex plain
    for i1 in range(0, size, pixel):
        for i2 in range(0, size, pixel):
            c1, c2 = (i1*resolution)-((resolution*size)-(resolution*size*0.25)), \
                     (i2*resolution)-((resolution*size)-(resolution*size*0.5))
                                   # changes the from the for loop to the number
                                   # that is going to be checked for Mandelbrot-ness
            if i2 == 999 and i1 % 9 == 0:
                print("--- "+(str((int(i1)+1)/10)+'%')+", time elapsed in seconds: %s ---" % (time.time() - start_time))
                # just prints the percentage done and how long it took
            c = check(c1, c2)
            cnv.create_rectangle(i1, i2, i1+pixel, i2+pixel, fill=color_map(c), width=0)
            # ^^^ creates each pixel with a specific colour


start_time = time.time()  # starts the timer
main = Tk()  # basic GUI stuff here
cnv = Canvas(main, width=1000, height=1000)

cnv.pack()

fractal()

print("--- finished in %s seconds ---" % (time.time() - start_time))

mainloop()
