Locations = [["Sydney", 326], ["Tonga", 378], ["Shanghai", 1436], ["London", 2376]]
Departures = [["Christchurch", 75], ["Wellington", 50], ["Auckland", 0]]
Accomadation = [["Sydney", 120], ["Tonga", 40], ["Shanghai", 60], ["London", 80]]

Total_Price = 0


print("Welcome to the flight calculator, please answer the questions below acurately")

value = 0
listno = 1
ask = True
while ask == True:
    if value == len(Locations):
        ask = False
    else:
        print(listno, ":", Locations[value][0])
        value+=1
        listno+=1

destination = int(input("Where will you be travelling to? (Please answer with the nunmber of the country)"))
destination-=1
Total_Price+= (Locations[destination][1])



departure_value = 0
departure_no = 1
loop = True
while loop == True:
    if departure_value == len(Departures):
        loop = False
    else:
        print(departure_no, ":", Departures[departure_value][0])
        departure_value+=1
        departure_no+=1

departure = int(input("Where are you departing from? (Please answer with the number of the city)"))
departure-=1
Total_Price+= (Departures[departure][1])



stay = int(input("How many nights are you staying?"))
Total_Stay = stay*(Accomadation[destination][1])
Total_Price+= Total_Stay
print("The total price you will be paying for the selected options is:", Total_Price, "NZD")