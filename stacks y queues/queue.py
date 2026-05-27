queue = []

queue.append(7)
queue.append(3)
queue.append(8)

for e in range(0, len(queue)):
    queue.pop(0)
    print(queue)
