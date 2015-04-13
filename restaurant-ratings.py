# your code goes here
def rating_sort(scores_filepath):
    scores = open(scores_filepath)
    restaurantscores = {}

    for restaurant in scores:
        restaurant = restaurant.rstrip()
        scorelist = restaurant.split(':')
        # restaurantname, score
        name, score = scorelist
        restaurantscores[name] = score

    alpha_restaurants = sorted(restaurantscores)

    for name in alpha_restaurants:
        score = restaurantscores.get(name, "does not exist")
        print "Restaurant %s is rated at %s." % (name, score)



rating_sort("scores.txt")