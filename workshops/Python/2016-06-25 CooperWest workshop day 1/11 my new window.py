from vanilla import Window, Slider, Button  # or from vanilla import *

w = Window((400, 300), "My new window")

w.mySlider = Slider((10, 10, 200, 20))
w.myButton = Button((10, 40, 100, 20), "Click me!")

w.open()
