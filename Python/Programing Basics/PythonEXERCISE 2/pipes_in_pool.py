v = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

first_pipe = P1 * H
second_pipe = P2 * H
both_pipes = first_pipe + second_pipe

first_percent = (first_pipe / both_pipes) * 100
second_percent = (second_pipe / both_pipes) * 100
both_percent = (both_pipes / v) * 100

if v >= both_pipes:
    print(f"The pool is {both_percent:.2f}% full. Pipe 1: {first_percent:.2f}%. Pipe 2: {second_percent:.2f}%.")
elif v < both_pipes:
    extra_liters = abs(v - both_pipes)
    print(f"For {H} hours the pool overflow with {extra_liters} liters.")