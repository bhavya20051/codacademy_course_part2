"""

Build a Tourism Recommendation Engine
The Boredless Tourist
Welcome to The Boredless Tourist, an online application giving you the power to find the parts of the city that fit the pace of your life. We at The Boredless Tourist run a recommendation engine using Python. We first evaluate what a person’s interests are and then give them recommendations in their area to venues, restaurants, and historical destinations that we think they’ll be engaged by. Let’s get started!

"""




destinations=["Paris,France","Shanghai,China","Los Angeles,USA","Sao Paulo, Brazil", "Cairo,Egypt"]

test_traveler= ["Erin Wilkes", "Shanghai,China", ["historical site", "art"]]

def get_destination_index(destination):
  destination_index=destinations.index(destination)
  return destination_index

print(get_destination_index("Los Angeles,USA"))
print(get_destination_index("Paris,France"))

def get_traveler_location(traveler):
  traveler_destination = test_traveler[1]   
  traveler_destination_index=get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index=(get_traveler_location(test_traveler))
print(test_destination_index)

attractions=[[],[],[],[],[]]

def add_attractions(destination,attraction):
  d_i=get_destination_index(destination)
  a_f_d=attractions[d_i]
  a_f_d.append(attraction)
  return
add_attractions("Los Angeles,USA",["Venice Beach", ["beach "]])
add_attractions("Paris,France", ["the Louvre", ["art", "museum"]])
add_attractions("Paris,France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attractions("Shanghai,China", ["Yu Garden", ["garden", "historcical site"]])
add_attractions("Shanghai,China", ["Yuz Museum", ["art", "museum"]])
add_attractions("Shanghai,China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attractions("Los Angeles,USA", ["LACMA", ["art", "museum"]])
add_attractions("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attractions("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attractions("Cairo,Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attractions("Cairo,Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination,interests):
  d_i=get_destination_index(destination)
  attractions_in_city=attractions[d_i]
  attractions_with_interest=[]
  for attraction in attractions_in_city:
    possible_attraction=[attraction]
    possible_attraction.append(attraction)
    attractions_tags=attraction[1]
    for interest in interests:
     if interest in attractions_tags:
       attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts=find_attractions("Los Angeles,USA",["art"]) 
print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination=traveler[1]
  traveler_interests=traveler[2]
  traveler_attractions=find_attractions(traveler_destination,traveler_interests)
  interests_string="Hi "+traveler[0]+", we think you'll like these places around "+ traveler_destination
  for attraction in traveler_attractions: 
    interests_string += " the "+ attraction[0] + ", "
    return interests_string

smills_france=get_attractions_for_traveler(["Derick Smill","Paris,France",["monument"]])

print(smills_france)