class Person:
    def __init__(self):
        self.arm = 2
        self.leg = 2

    def num_legs(self):
        print(self.leg)

if __name__=='__main__':
    david = Person()
    legs = david.num_legs()
