# add phone numbers here in this empty list that need to have text added for log of changes
# example [319*******, 319*******] the last number in the list do not have a comma
phone = []

# For the desired text to be used uncomment that line so then it prints that list with desired text
# Comment lines that you do not need so it will not print the text you do not want
# To comment line you do ctrl + / sign on that line
# To uncomment same thing as commenting a line

for item in phone:
    ## use this for when the phone number is not found in frames cutsheet and doesn't have a group ##
    print(f"Removed-{item} from BR&FT since it was taken out of cut sheet and no group assigned")
    
    ## use for when phone number is has no bridge appearance in the BR&FT sheet ##
    # print(f"Removed-{item} from BR&FT doesn't have any bridge appearances")
    
	# Backburner reasons to use
    # print(f"{item} - Could not find device, moved to backburner")
    # print(f"{item} - Moved skype account to backburner")
    # print(f"{item} - Moved ACD line to backburner")
    # print(f"{item} - Line and phone not needed anymore. Moved to Backburner.")
    # print(f"{item} - Virtual Phone line not needed and can be disconnected, moved to the backburner.")
    # print(f"{item} - Moved Fax Line to Backburner")