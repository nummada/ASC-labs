"""
    Basic thread handling exercise:

    Use the Thread class to create and run more than 10 threads which print their name and a random
    number they receive as argument. The number of threads must be received from the command line.

    e.g. Hello, I'm Thread-96 and I received the number 42

"""
import sys
from random import randint, seed
from threading import Thread

class MyThread(Thread):
    def __init__(self, nr, received_number):
        Thread.__init__(self)
        self.nr = nr
        self.received_number = received_number

    # thread function
    def run(self):
        print ("Hello, I'm Thread-" + str(self.nr), " and I received the number", self.received_number)

if __name__ == "__main__":
    seed()
    
    # threads list
    thread_list = []

    number_of_threads = int(sys.argv[1])

    #create threads
    for i in range(number_of_threads):
        thread = MyThread(i, randint(0, 1000))
        thread.start()
        thread_list.append(thread)
    
