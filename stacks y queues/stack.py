stack = []

stack.append(5)
stack.append(7)
stack.append(2)

for e in range(0, len(stack)):
    stack.pop()

    print(stack)