apartament_size = int(input()) * int(input()) * int(input())

total_boxes_size = 0

while True:
    boxes = input()

    if boxes == "Done":
        print(f"{apartament_size - total_boxes_size} Cubic meters left.")
        break

    boxes_count = int(boxes)
    total_boxes_size += boxes_count

    if total_boxes_size > apartament_size:
        print(f"No more free space! You need {total_boxes_size - apartament_size} Cubic meters more.")
        break
