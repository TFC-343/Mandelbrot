# code by TFC(James Packham)
# 28-11-2019
#

from tkinter import *
from complex_maths import complex_maths_float as comp
from complex_maths import comparative
from math import sqrt
import time


global resolution
global size  # i know i really shouldn't use global but im lazy
resolution = 160000  # how many rectangels in the whole thing
size = 1000  # size of the canvas, changing these does however break it a tad as i never got round to adding it in


resolution = (sqrt(resolution))/1000


# this bit shows the pos of the curser
def motion(event):
    global view
    # global resolution
    x, y = event.x, event.y
    a, b = (resolution*x)-((resolution*size)-(resolution*size*0.75)), (resolution*y)-((0.4*size)-(resolution*size*0.5))
    print('{}, {}'.format(int(a), int(b)))


def check(r, f):
    z = '0+0i'
    loops = 0
    # this loop iterated the code untill it either gets to big or we hit 500 loops
    while comparative(z, '2500+2500i', '<') > 1 and comparative(z, '-2500-2500i', '>') > 1 and loops < 500:
        z = comp(comp(str(z), str(z), 'times'), str(r/100)+'+'+str(f/100)+'i', 'add')
        loops += 1
    if comparative(z, '1000+1000i', '<') > 1:
        return 'black'  # sets it to black if the sequence does not tend towards infinity (is more than 1000 after
                        # 500 iterations)
    else:
        return 'white'  # sets it to white


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
            cnv.create_rectangle(i1, i2, i1+pixel, i2+pixel, fill=c, width=0)
            # ^^^ creates each pixel with a specific colour


start_time = time.time()  # starts the timer
main = Tk()  # basic GUI stuff here
cnv = Canvas(main, width=1000, height=1000)

cnv.pack()

fractal()

print("--- finished in %s seconds ---" % (time.time() - start_time))

mainloop()
