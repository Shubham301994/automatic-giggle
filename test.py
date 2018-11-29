#class Person:
#    def __init__(self):
#        self.arm = 2
#        self.leg = 2
#
#    def num_legs(self):
#        print(self.leg)
#
#if __name__=='__main__':
#    david = Person()
#    legs = david.num_legs()

import numpy as np

x = np.array([0,10,27,35,44,32,56,35,87,22,47,17])
x = np.arange(0, x.size, 3)

print(x)
