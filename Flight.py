Locations = [["Sydney", 326], ["Tonga", 378], ["Shanghai", 1436], ["London", 2376]]
Departures = [["Christchurch", 75], ["Wellington", 50], ["Auckland", 0]]
Accomadation = [["Sydney", 120], ["Tonga", 40], ["Shanghai", 60], ["London", 80]]


departure = input("Where is your departure location?")
travel_location = input("Where are you Traveling to?")
acom = int(input("How many nights are you staying at this location?"))

value = 0
ask = True
while ask == True:
    print(locations[value][0])
    value+=1
    departure = input("Where is your departure location?")