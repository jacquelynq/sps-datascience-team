import ipywidgets as wd
from vpython import *
scene = canvas() # This is needed in Jupyter notebook and lab to make programs easily rerunnable

# This version uses a Jupyter notebook menu
# See Textures2 for a version that uses a VPython menu

scene.width = 600
scene.height = 600

R = 0.4 # radius of sphere
D = 0.7 # size of box
c = sphere(pos=vec(0,0,0), size=D*vec(1,1,1))
c.texture = textures.earth
