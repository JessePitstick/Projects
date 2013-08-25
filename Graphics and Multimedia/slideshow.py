"""
Slide Show - An application that shows various
pictures in a slideshow format

Dependencies: collections.deque for class SlideShow
"""

from collections import deque
import time
import pyglet

class SlideShow:

    def __init__(self, pictures=None, interval=5, playing=False):
        """Initialize the Slide Show"""
        self._pictures = deque()
        if pictures:
            for picture in pictures:
                self.add_picture(picture)
        self._interval = interval
        self._playing = playing
        
    def add_picture(self, picture):
        """Add a picture to the slideshow"""
        if picture not in self._pictures:
            self._pictures.append(picture)
        else:
            self._pictures.append(picture)
        return
        
    def next_picture(self):
        """Shuffles pictures and returns next picture if there is at least one picture, 
           Returns None if there are no pictures"""
        if self._pictures:
            self._pictures.rotate(-1)
            return self._pictures[0]
        else:
            return None
            
    def pause(self):
        """Pauses the slideshow"""
        self._playing = False
        
    def play(self):
        """Plays the slideshow"""
        self._playing = True
    
    def is_playing(self):
        return self._playing

    def set_interval(self, interval):
        """Sets the time interval in s"""
        self._interval = interval

    def get_interval(self):
        return self._interval
        
if __name__ == '__main__':
    
    list_of_pictures = ['sample1.jpg', 'sample2.jpg', 'sample3.jpg']
    slideshow = SlideShow(pictures=list_of_pictures)

    window = pyglet.window.Window()
    image = None
    
    #slideshow.pause()
    slideshow.set_interval(1)
    slideshow.play()

    @window.event
    def on_draw():
        time.sleep(slideshow.get_interval())
        if slideshow.is_playing():
            image = pyglet.image.load(slideshow.next_picture())
            window.clear()
            image.blit(0,0)

    pyglet.app.run()
