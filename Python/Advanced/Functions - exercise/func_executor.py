def func_executor(*func_info):
    return "\n".join(f"{func_name.__name__} - {func_name(*values)}" for func_name,values in func_info)

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
