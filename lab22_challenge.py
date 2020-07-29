farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

#easy
animals = farms[0]["agriculture"]
for x in animals:
    print(x)

#Medium
farm = input("Choose a farm (NE Farm, W Farm, or SE Farm)")
if farm == "NE Farm":
    animals_plants = farms[0]["agriculture"]
    for x in animals_plants:
        print(x)

elif farm == "W Farm":
    animals_plants = farms[1]["agriculture"]
    for x in animals_plants:
        print(x)

elif farm == "SE Farm":
    animals_plants = farms[2]["agriculture"]
    for x in animals_plants:
        print(x)

#Hard
farm = input("Choose a farm (NE Farm, W Farm, or SE Farm)")

if farm == "NE Farm":
    animals_plants = farms[0]["agriculture"]

    for x in animals_plants:
        print(x)

elif farm == "W Farm":
    animals_plants = farms[1]["agriculture"]
    for x in animals_plants:
        print(x)

elif farm == "SE Farm":
    animals_plants = farms[2]["agriculture"][0]
    for x in animals_plants:
        print(x, end='')
    print("")
