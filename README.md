# Dino_run
03/07/2019: Chrome's dinosaur run but self made with [Processing](https://py.processing.org/). A simple project to test some ideas I had for a while. Feel free to hit me up with suggestions or ideas!!

## Objects

### Dino

This is an object to implement the dinosaur. It has an `xpos` and a `ypos` parameters to store its position and a `yspeed`
to store the vertical speed. It also has an `anim` variable that works internally to manage the animation.

#### Methods

* `display()`: This simple method must be called every frame to display the Dinosaur. Its only complexity lies in cycling through 
the two frames to make it animated. It does this by incrementing the parameter `anim` until it reaches its limit and resetting it.
* `drive()`: This methods updates the position and must be called every frame. It substracts the speed from the position 
and gravity's acceleration from speed to make the movement look realistic. It also checks whether it has hit the ground in
order to stop the fall.
* `jump()`: It updates the vertical speed in order to start a jump.
