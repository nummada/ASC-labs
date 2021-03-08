from threading import Semaphore, Thread
import time

number_of_philosofers = 8
forks = []

class Philosofer(Thread):
    """class that represents a philosofer"""
    def __init__(self, thread_id, left_idx, right_idx):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.left_idx = left_idx
        self.right_idx = right_idx

    def run(self):
        """run function from Thread"""
        
        # the first philosopher takes first the left fork, then the right fork
        if self.thread_id == 0:
            forks[self.left_idx].acquire()
            forks[self.right_idx].acquire()
            time.sleep(1)
            print("Philosofer number " + str(self.thread_id) + " is eating")
            forks[self.right_idx].release()
            forks[self.left_idx].release()
        else:
            forks[self.right_idx].acquire()
            forks[self.left_idx].acquire()
            time.sleep(1)
            print("Philosofer number " + str(self.thread_id) + " is eating")
            forks[self.left_idx].release()
            forks[self.right_idx].release()

if __name__ == '__main__':

    for i in range(number_of_philosofers):
        forks.append(Semaphore(value = 1))

    for i in range(number_of_philosofers):
        left_idx = i
        right_idx = (i+1) % number_of_philosofers
        thread = Philosofer(i, left_idx, right_idx)
        thread.start()
        