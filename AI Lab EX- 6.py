
room = {'A': 'Dirty', 'B': 'Dirty'}
position = 'A'

while 'Dirty' in room.values():
    print("Vacuum cleaner is in room", position)

    if room[position] == 'Dirty':
        room[position] = 'Clean'
        print(position, "room cleaned")

    if position == 'A':
        position = 'B'
    else:
        position = 'A'

print("Final status:", room)
print("All rooms are clean")
