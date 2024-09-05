

def join_names(firstname, lastname):
    if len(firstname) != len(lastname):
        print("First and Last name lists are not the same length")
    username = [f"{first} {last}" for first, last in zip(firstname, lastname)]
    return username

phone = [3192020156]
userfirst = ["dillon"]
userlast = ["bender"]

full_name = join_names(userfirst, userlast)


for phone, name in zip(phone, full_name):
    print(f"{phone} - Removed from cutover {name} doesn't have a healthcare account")
