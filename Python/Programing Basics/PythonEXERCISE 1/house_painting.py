x = float(input())
y = float(input())
h = float(input())

LITER_GREEN_PAINT = 3.4
LITER_RED_PAINT = 4.3
WINDOW_SIDE  = 1.5
DOOR_WIDHT = 1.2
DOOR_HEIGHT = 2

door_area = DOOR_WIDHT * DOOR_HEIGHT

side_wall = x * y
window_area = WINDOW_SIDE * WINDOW_SIDE
both_side_walls = side_wall * 2 - window_area * 2

back_wall = x * x
front_wall = x * x - door_area
front_and_back_walls = back_wall + front_wall
total_area_sides = both_side_walls + front_and_back_walls

green_paint = total_area_sides / LITER_GREEN_PAINT

two_roof_rectangles = 2 * (x * y)
two_roof_triangles = 2 * (x * h / 2)
total_area_roof = two_roof_triangles + two_roof_rectangles

red_paint = total_area_roof / LITER_RED_PAINT

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")




