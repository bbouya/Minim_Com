""""
First lets use a command line interface to create a scene the class through which Maning generates videos.



"""

# import library to draw circle : 
from manim import * 

class CreateCircle(Scene):
    def construct(self):
        circle = Circle() # Create circle
        circle.set_fill(PINK, opacity=0.5) # Set the color and transparency
        self.play(Create(circle))


