if __name__ == "__main__": raise SystemError("Incorrect starting file")

class PicLayer(object):
    def __init__(self, name, surface):
        self.name = name
        self.surface = surface

        self.position = (0,0)
        self.velocity = (0,0)

    def set_position(self, poz):
        self.position = poz
    
    def set_velocity(self, vel):
        self.velocity = vel
