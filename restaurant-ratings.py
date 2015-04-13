# your code goes here
def rating_sort(scores_filepath):
    scores = open(scores_filepath)
    restaurantscores = {}

    for restaurant in scores:
        restaurant = restaurant.rstrip()
        #This will work, but scorelist is confusing as a name here:
        scorelist = restaurant.split(':')
        name, score = scorelist

        # This is a single line to do what is the two lines previously:
        # name, score = restaurant.split(':')

        # Change the strings of numbers into int as soon as you can 
        # to prevent issues later on: 
        restaurantscores[name] = int(score)

    # To remind yourself that sorted returns a list of the key values
    # add .keys() to the dictionary when calling it.
    alpha_restaurants = sorted(restaurantscores.keys())

    for name in alpha_restaurants:
        score = restaurantscores.get(name, "does not exist")
        print "Restaurant %s is rated at %s." % (name, score)

    


rating_sort("scores.txt")