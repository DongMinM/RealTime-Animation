import matplotlib.pyplot as plt
import matplotlib.animation as animation

import threading
from queue import Queue

import rospy
from std_msgs.msg import String


class Animator:
    def __init__(self):

        self.n_q = Queue()
        self.e_q = Queue()
        self.v_q = Queue()
        self.n = []
        self.e = []
        self.v = []

        self.animate_run()

        rospy.init_node('animator')
        rospy.Subscriber('gps',String,self.readData,queue_size=1)
        rospy.spin()

    def animate(self,i):
        plt.cla()
        plt.xlim([0,1])
        plt.ylim([0,1])

        self.n.append(self.n_q.get())
        self.e.append(self.e_q.get())


        plt.plot(self.n,self.e,self.v)

    def animate_run(self):
        fig = plt.figure()
        animate = animation.FuncAnimation(fig,self.animate, interval=1)
        plt.show()


    def readData(self, msg):
        lati = msg[1]
        longi = msg[2]
        h = msg[3]
        
        self.ned2nev(lati,longi,h)
        
    def ned2nev(self,lati,longi,h):
        pass







if __name__ == '__main__':
    animator = Animator()
