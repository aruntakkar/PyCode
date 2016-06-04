import threading


class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())


x = Messenger(name='send out messages')
y = Messenger(name='receive messages')
x.start()
y.start()
