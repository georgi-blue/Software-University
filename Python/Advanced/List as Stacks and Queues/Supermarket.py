from collections import deque

text = input()

supermarket_queue = deque()

while text != "End":
    if text == "Paid":
        while supermarket_queue:
            print(supermarket_queue.popleft())
    else:
        supermarket_queue.append(text)
    text = input()

print(f"{len(supermarket_queue)} people remaining.")