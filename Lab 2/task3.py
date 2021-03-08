"""
Coffee Factory: A multiple producer - multiple consumer approach

Generate a base class Coffee which knows only the coffee name
Create the Espresso, Americano and Cappuccino classes which inherit the base class knowing that
each coffee type has a predetermined size.
Each of these classes have a get message method

Create 3 additional classes as following:
    * Distributor - A shared space where the producers puts coffees and the consumers takes them
    * CoffeeFactory - An infinite loop, which always sends coffees to the distributor
    * User - Another infinite loop, which always takes coffees from the distributor

The scope of this exercise is to correctly use threads, classes and synchronization objects.
The size of the coffee (ex. small, medium, large) is chosen randomly everytime.
The coffee type is chosen randomly everytime.

Example of output:

Consumer 65 consumed espresso
Factory 7 produced a nice small espresso
Consumer 87 consumed cappuccino
Factory 9 produced an italian medium cappuccino
Consumer 90 consumed americano
Consumer 84 consumed espresso
Factory 8 produced a strong medium americano
Consumer 135 consumed cappuccino
Consumer 94 consumed americano
"""
import random
from threading import Lock, Semaphore, Thread
import time

MAX_NUMBER_OF_COFFEES = 15
NUMBER_OF_COFFEE_FACTORIES = 10
NUMBER_OF_USERS = 30
# sleep for testing
SLEEP_TIME = 0.5

class Coffee:
    """ Base class """
    def __init__(self, name):
        self.name = name
        self.size = random.choice(["small", "medium", "large"])

    def get_name(self):
        """returns the name of the coffee"""
        return self.name

    def get_size(self):
        """returns the size of the coffee"""
        return self.size


class Espresso(Coffee):
    """ Espresso implementation """
    def __init__(self):
        self.type = "Espresso"
        self.attribute = "nice"
        Coffee.__init__(self, self.type)

    def get_message(self):
        """returns the message to be printed by distributor"""
        message = self.attribute + " " + self.size + " " + self.type
        return message


class Americano(Coffee):
    """ Americano implementation """
    def __init__(self):
        self.type = "Americano"
        self.attribute = "strong"
        Coffee.__init__(self, self.type)

    def get_message(self):
        """returns the message to be printed by distributor"""
        message = self.attribute + " " + self.size + " " + self.type
        return message

class Cappuccino(Coffee):
    """ Cappuccino implementation """
    def __init__(self):
        self.type = "Cappuccino"
        self.attribute = "italian"
        Coffee.__init__(self, self.type)

    def get_message(self):
        """returns the message to be printed by distributor"""
        message = self.attribute + " " + self.size + " " + self.type
        return message


class Distributor:
    """class that represents the distributor of coffees"""
    def __init__(self):
        self.produced_coffee = []
        self.max_number_of_coffees = MAX_NUMBER_OF_COFFEES

    def add_coffee(self, coffee, factory_number):
        """function that produces coffee"""
        self.produced_coffee.append(coffee)
        print("Factory " + str(factory_number) + " produced a " + coffee.get_message())

    def remove_coffee(self, consumer_number):
        """function that consumes coffee"""
        coffee = self.produced_coffee[0]
        self.produced_coffee.pop(0)
        print("Consumer " + str(consumer_number) +  " consumed " + coffee.get_name())


class CoffeeFactory(Thread):
    """class that represents a coffee factory"""
    def __init__(self, empty, full, lock, factory_id):
        Thread.__init__(self)
        self.empty = empty
        self.full = full
        self.lock = lock
        self.distributor = distributor
        self.factory_id = factory_id

    def run(self):
        while True:
            empty_sem.acquire()
            self.lock.acquire()

            # for testing purpose
            time.sleep(SLEEP_TIME)

            produced_coffee = None
            random_no = random.choice([0, 1, 2])
            if random_no == 0:
                produced_coffee = Espresso()
            elif random_no == 1:
                produced_coffee = Americano()
            else:
                produced_coffee = Cappuccino()

            distributor.add_coffee(produced_coffee, self.factory_id)

            self.lock.release()
            full_sem.release()


class User(Thread):
    """class that represents a buyer"""
    def __init__(self, empty, full, lock, user_id):
        Thread.__init__(self)
        self.empty = empty
        self.full = full
        self.lock = lock
        self.distributor = distributor
        self.user_id = user_id

    def run(self):
        while True:
            full_sem.acquire()
            self.lock.acquire()

            # for testing purpose
            time.sleep(SLEEP_TIME)

            distributor.remove_coffee(self.user_id)

            self.lock.release()
            empty_sem.release()

if __name__ == '__main__':

    distributor = Distributor()
    empty_sem = Semaphore(value = distributor.max_number_of_coffees)
    full_sem = Semaphore(value = 0)
    my_lock = Lock()


    users_list = []
    for i in range(NUMBER_OF_USERS):
        thread = User(empty_sem, full_sem, my_lock, i)
        thread.start()
        users_list.append(thread)

    factory_list = []
    for i in range(NUMBER_OF_COFFEE_FACTORIES):
        thread = CoffeeFactory(empty_sem, full_sem, my_lock, i)
        thread.start()
        factory_list.append(thread)
