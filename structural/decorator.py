from time import time, sleep


def decorator(func):
    def timer():
        start = time()
        func()
        stop = time()
        return stop - start
    return timer


if __name__ == "__main__":

    @decorator
    def main():
        print("Start")
        sleep(2)
        print("Stop")



