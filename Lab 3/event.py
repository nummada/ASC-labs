from threading import enumerate, Event, Thread, Condition


class Master(Thread):
    def __init__(self, max_work, condition):
        Thread.__init__(self, name = "Master")
        self.max_work = max_work
        self.condition = condition
    
    def set_worker(self, worker):
        self.worker = worker
    
    def run(self):
        for i in range(self.max_work):

            # get the condition lock
            condition.acquire()
            # generate work
            self.work = i

            # notify worker
            condition.notify()
            condition.release()

            # wait for worker
            condition.acquire()
            condition.wait()

            # get result
            if self.get_work() + 1 != self.worker.get_result():
                print ("oops")
            print ("%d -> %d" % (self.work, self.worker.get_result()))

            #notify worker
            condition.notify()
            condition.release()
    
    def get_work(self):
        return self.work

class Worker(Thread):
    def __init__(self, terminate, condition):
        Thread.__init__(self, name = "Worker")
        self.terminate = terminate
        self.condition = condition

    def set_master(self, master):
        self.master = master
    
    def run(self):
        while(True):
            # wait work
            condition.acquire()
            condition.wait()

            if(terminate.is_set()): break

            # generate result
            self.result = self.master.get_work() + 1

            # notify master
            condition.notify()
            condition.release()
            
    
    def get_result(self):
        return self.result

if __name__ ==  "__main__":
    # create shared objects
    terminate = Event()
    condition = Condition()
    
    # start worker and master
    w = Worker(terminate, condition)
    m = Master(10, condition)
    w.set_master(m)
    m.set_worker(w)
    w.start()
    m.start()

    # wait for master
    m.join()

    terminate.set()
    # notify worker
    condition.acquire()
    condition.notify()
    condition.release()
    
    # wait for worker
    w.join()

    # print running threads for verification
    print(enumerate())

