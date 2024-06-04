
import multiprocessing as mp
import time
import random
import traceback


class Process(mp.Process):
    def __init__(self, *args, **kwargs):
        mp.Process.__init__(self, *args, **kwargs)
        self._pconn, self._cconn = mp.Pipe()
        self._exception = None

    def run(self):
        try:
            mp.Process.run(self)
            self._cconn.send(None)
        except Exception as e:
            tb = traceback.format_exc()
            self._cconn.send((e, tb))
            raise e  # You can still rise this exception if you need to

    @property
    def exception(self):
        if self._pconn.poll():
            self._exception = self._pconn.recv()
        return self._exception


def loop_one():
    try:
        while True:
            sleep = random.randrange(1, 5)
            print(f'loop one, wait for {sleep} seconds')
            time.sleep(sleep)
            raise Exception('loop one exception')
    except Exception as e:
        print(f'loop one exception: {e}')
        loop_one()


def loop_two():
    while True:
        sleep = random.randrange(1, 5)
        print(f'loop two wait for {sleep} seconds')
        time.sleep(sleep)
        # raise Exception('HORRIBLE EXCEPTION')


def run():
    p1 = mp.Process(target=loop_one, daemon=True)
    p2 = mp.Process(target=loop_two, daemon=True)

    p1.start(), p2.start()

    #p1.join(), p2.join()

    """if p1.exception:
            error, traceback = p1.exception
            print(f'p1 exception caught: {error}')
    
        if p2.exception:
            error, traceback = p2.exception
            print(f'p2 exception caught: {error}')"""

    while True:
        try:
            time.sleep(5)
            print('MAIN LOOP')
        except KeyboardInterrupt as e:
            print('MAIN LOOP INTERRUPTED')
            break


def sync_run():
    loop_one()
    loop_two()


if __name__ == '__main__':
    run()
    #sync_run()
