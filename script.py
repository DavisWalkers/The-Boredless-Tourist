# Destinations list
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
# Test case
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# Get index from a string
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

# Get index from a traveler list
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

# Testing functions
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

# Visiting Interesting Places
attractions = [[] for dest in destinations]
print(attractions)

# Adding new attractions to the attractions list
def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
    except ValueError:
        return
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return 

# Adding some attractions
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# Finding attractions based on traveler's interests
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for possible_attraction in attractions_in_city:
        attraction_tags = possible_attraction[1]
        for interest in interests:
            if (attraction_tags.count(interest) != 0):
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

# Testing
la_arts = find_attractions("Los Angeles, USA", ['art'])
print(la_arts)

# Making a string with all attractions for a traveler
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = "Hi "
    interests_string += traveler[0]
    interests_string += ", we think you'll like these places around " + traveler_destination + ":"

    for i in range(len(traveler_attractions) - 1):
        interests_string += " " + traveler_attractions[i] + ","
    interests_string += " " + traveler_attractions[len(traveler_attractions) - 1] + "."
    return interests_string

# Testing
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
