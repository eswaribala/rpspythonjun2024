import os
import multiprocessing

def notepadprocess():
    print("ID of process running worker1: {}".format(os.getpid()))
    os.system('notepad')


def excelprocess():
    print("ID of process running worker1: {}".format(os.getpid()))
    os.system('dir')


if __name__ == '__main__':
    print("ID of main process: {}".format(os.getpid()))

    # creating processes
    p1 = multiprocessing.Process(target=notepadprocess)
    p2 = multiprocessing.Process(target=excelprocess)

    # starting processes
    p1.start()
    p2.start()

    # process IDs
    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))

    # wait until processes are finished
    p1.join()
    p2.join()

    # both processes finished
    print("Both processes finished execution!")

    # check if processes are alive
    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))