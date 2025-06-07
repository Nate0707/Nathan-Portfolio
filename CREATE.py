# Digital realestate
community_list = ["Pilsen", "Greek Town", "Logan Square", "Little Italy", "West Town", "River North", "Lincon park", "The Loop", "Hyde Park", "Wicker Park", "Gold Coast", "West Loop", "Edgewater", "Streeterville" ]
avgrent_appt = [1600, 2291, 1600, 1650, 2173, 2900, 1600, 2700, 1300, 1600, 1700, 2600, 1300, 1900]
Real = []

print("Welcome to fine what neigborhood your new apartment will be in")
print("price per month for cheap will be 1900 or less , for moderate it will be more than 1900 but less then 2200, and expensive will be more than 2200")
price = input("Please enter cheap, moderate, or expensive depending on how much you want to spend. ")#input


def digital_relaestat(price): # perameter

    if price == "cheap":
        for i in range(len(community_list)): #loop
            if avgrent_appt[i] <= 1900: # if statment
                Real.append(community_list[i])
        print(Real)

    if price == "moderate":
        for i in range(len(community_list)): #loop
            if avgrent_appt[i] > 1900 and  avgrent_appt[i] < 2200: # if statment
                Real.append(community_list[i])
        print(Real)

    if price == "expensive":
        for i in range(len(community_list)): #loop
            if avgrent_appt[i] >= 2200: # if statment
                Real.append(community_list[i])
        print(Real)



digital_relaestat(price) # call function
