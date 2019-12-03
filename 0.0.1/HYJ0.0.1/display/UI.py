#should not start from this file
if __name__ == "__main__": raise SystemError("Incorrect starting file")



#define the "Pic" class, used to hold a picLayer with it's velocity and acceleration.
class Pic(object):

    #initialize the object with necessary information
    def __init__(self, surface,\
            position     = (0,0) ,\
            velocity     = (0,0) ,\
            acceleration = (0,0) ):
        
        #declare the information arguments as the object's attributes
        self.surface      = surface
        self.position     = position
        self.velocity     = velocity
        self.acceleration = acceleration

        #declare a attibute for owner indication
        self.page = None


    #update the velocity and the acceleration of the picLayer
    def update(self):

        #run for both X and Y value for the vectors
        for axis in [0,1]:
            self.velocity[axis] += self.acceleration[axis]
            self.position[axis] += self.velocity[axis]


    #paint the picLayer
    def blit(self):
        self.page.surface.blit(
            self.surface, self.position
        )



#define the "Page" class, used to hold and use some picLayers
class Page(object):

    #initialize the object with necessary information
    def __init__(self, )