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

    def update(self):
        if self.velocity != (0,0):
            self.position = ( 
                self.position[0] + self.velocity[0] ,\
                self.position[1] + self.velocity[1]
            )
        print("debug")


class PicPool(object):
    def __init__(self):
        self.pool = {}

    def new_PicLayer(self, PL):
        assert type(PL) == PicLayer
        self.pool[PL.name] = PL

    def remove_PicLayer(self, name):
        try:
            del self.pool[name]
        except KeyError:
            pass

    def update(self):
        for PL in self.pool:
            PL.update()
