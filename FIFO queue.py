from queues import Queue

fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

fifo.dequeue()

fifo.dequeue()

fifo.dequeue()

fifo = Queue("1st", "2nd", "3rd")
len(fifo)


for element in fifo:
    print(element)





len(fifo)