from collections import deque

expression = deque(input())
open_parenthesis = deque()

while expression:
    current_expression = expression.popleft()

    if current_expression in "({[:":
        open_parenthesis.append(current_expression)

    elif not open_parenthesis:
        print("NO")
        break
    else:
        if f"{open_parenthesis.pop() + current_expression}" not in "(){}[]":
            print("NO")
            break

else:
    print("YES")