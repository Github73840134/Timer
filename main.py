from Timer import Timer
import time
import os
t1 = Timer(1)
t1.init(1,Timer.PERIODIC,False,lambda:print('Timer1 Is Done'))
t1.start()