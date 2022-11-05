from heap_queue import HeapQueue

heap_Queue = HeapQueue()

heap_Queue.enqueue("1")
heap_Queue.enqueue("2")
heap_Queue.enqueue("3")
heap_Queue.enqueue("4")
heap_Queue.enqueue("5")

print(heap_Queue.__len__())

print(heap_Queue.is_empty())

print(heap_Queue.first())

print(heap_Queue.dequeue())