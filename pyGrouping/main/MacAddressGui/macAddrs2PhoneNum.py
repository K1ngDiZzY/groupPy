# useful VScode shortcuts control + alt + shift and then use arrow keys to place commas ect.

def sort_dict_by_list(input_dict, sort_list):
    return {key: input_dict[key] for key in sort_list if key in input_dict}


# phone number is the key and mac address is the value
#  example 319*******: "50***********",
numbersWithMac = {}

# this is for the phone numbers that are sorted in order from Excel sheet
phSorted_list = []

# this sorts the numbers with the mac by the way it is sorted in Excel
sorted_dict = sort_dict_by_list(numbersWithMac, phSorted_list)

# this prints the mac address to copy back over into the Excel sheet
for key, value in sorted_dict.items():
    print(f"{value}")
