
# Task 3: Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(self.queue)


print("=" * 45)
print("TASK 3: Queue Implementation")
print("=" * 45)

q = Queue()
q.enqueue(100)
q.enqueue(200)
q.enqueue(300)
print("Queue after enqueue:")
q.display()
print("Front element:", q.front())
print("Dequeued element:", q.dequeue())
print("Queue after dequeue:")
q.display()


# Task 4: Customer Service Simulation
def customer_service(customers):
    service_queue = Queue()

    for customer in customers:
        service_queue.enqueue(customer)

    print("\nCustomers waiting:")
    service_queue.display()

    while not service_queue.is_empty():
        served = service_queue.dequeue()
        print(f"Serving customer: {served}")
        print("Remaining queue:")
        service_queue.display()


print("\n" + "=" * 45)
print("TASK 4: Customer Service Simulation")
print("=" * 45)

customer_service(['Sonam', 'Pema', 'Karma'])