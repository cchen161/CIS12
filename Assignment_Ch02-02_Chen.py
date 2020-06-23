# Door input
door_length, door_width = input("Enter the length and width of the door: ").split(" ")
door_length = int(door_length)
door_width = int(door_width)

# Window 1 input
window1_length, window1_width = input("Enter the length and width of the first window: ").split(" ")
window1_length = int(window1_length)
window1_width = int(window1_width)

# Window 2 input
window2_length, window2_width = input("Enter the length and width of the second window: ").split(" ")
window2_length = int(window2_length)
window2_width = int(window2_width)

# Bookshelf input
bookshelf_length, bookshelf_width = input("Enter the length and width of the bookshelf: ").split(" ")
bookshelf_length = int(bookshelf_length)
bookshelf_width = int(bookshelf_width)

# Room input
room_length, room_width, room_height = input("Enter the length, width, and height of the room: ").split(" ")
room_length = int(room_length)
room_width = int(room_width)
room_height = int(room_height)
print()

# Area calculations
door_area = door_length * door_width
window1_area = window1_length * window1_width
window2_area = window2_length * window2_width
bookshelf_area = bookshelf_length * bookshelf_width
room_area = room_width * room_height

# Paint needed
paint_can = 120
paint_needed = (room_area * 4) - (door_area + window1_area + window2_area + bookshelf_area)
total_paint_needed = paint_needed / paint_can 
round_paint = round(total_paint_needed, 2)

print("The amount of paint needed to paint the room: {} gallons.".format(round_paint))
