def rectangle(lenght, width):

    if not isinstance(width, int) or not isinstance(lenght, int):
        return "Enter valid values!"

    def area():
        return width * lenght

    def perimeter():
        return 2 * (lenght + width)

    return f"Rectangle area: {area()} \nRectangle perimeter: {perimeter()} "

print(rectangle('2', 10))