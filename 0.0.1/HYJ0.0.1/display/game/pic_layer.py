if __name__ == "__main__": raise SystemError("Incorrect starting file")

class PicLayer(object):
    def __init__(self,
        position = (0,0) ,\
        velocity = (0,0) ):

        self.position     = position
        self.velocity     = velocity

    def update(self):
        for c in [0,1]:
            self.position[c] += self.velocity[c]
