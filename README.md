# Dino_run
03/07/2019: Chrome's dinosaur run but self made with [Processing](https://py.processing.org/). A simple project to test some ideas I had for a while. Feel free to hit me up with suggestions or ideas!!

03/08/2019:
## MAIN: `dino_game.pyde`
This file is the main file of the game, intended to be run with Processing, implemets
the main features of the game. It is written using Python Processing, which is a Python-based
language and environment made to be used for graphics programming, greatly simplifying the 
development.

The variables that handle every element are declared globally: `myCar1` and `parts`. The
first one is merely a container for a `Dino` object whereas the other is a [double-ended queue](https://en.wikipedia.org/wiki/Double-ended_queue) that will hold up to 100 particles.

As a Processing file, it has two main functions. The first one, `setup()`, is run
at the start of the program. In it, the window is initialized to a fixed size of 800x800 
and the framerate is locked to 30. The second one, `draw()`, contains the main logic
of the game to be run every frame. In it, the image is reset to continue plotting and handling
the logic for every item.



## Objects

### Dino

This is an object to implement the behaviour and plotting of the dinosaur. It has both `xpos` and a `ypos` parameters to store its position and a `yspeed` parameter
to store the vertical speed. It also has an `anim` parameter that works internally to manage the animation.

#### Methods

* `display()`: This simple method must be called every frame to display the Dinosaur. Its only complexity lies in cycling through 
the two frames to make it animated. It does this by incrementing the parameter `anim` until it reaches its limit and resetting it.
* `drive()`: This methods updates the position and must be called every frame. It substracts the speed from the position 
and gravity's acceleration from speed to make the movement look realistic. It also checks whether it has hit the ground in
order to stop the fall.
* `jump()`: It updates the vertical speed in order to start a jump.

### Particle

This object is used to implement the different aesthetic elements that appear on the ground. 
It has parameters for the position ( `xpos` and `ypos`), the kind of element it is ( 
`gusano`), a parameter to handle the animation ( `anim`) and a final parameter ( `splat`) to check if it has been stepped on. When it is 
built, it is assigned a random vertical position on the right edge of the screen and
it decides randomly whether it is a simple line (99%), a centipede (0.5%) or an scorpion
(0.5%).

#### Methods

* `plot()`: This method plots the element depending on the kind. If it is a centipede 
or a scorpion it cheks if it has been splatted and handles the animation just like the Dino
object.
* `move()`: This method moves the particle a fixed amount of pixels to the left to emulate
movement. If the particle is near the dinosaur and is an animal, it gets splatted.
