# This is for speed dials for the log of changes 
# put the numbers in the speed dial list make sure to have a comma after each number and a space
# do not put a comma after the last number in the list
speedDial = []


# This is adding an actual comma when printed
addingComma = ', '.join(map(str, speedDial))

# prints what needs to be done
print(f"Removed Speed Dial(s) - {addingComma}")
