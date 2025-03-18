def get_friends_favorite_candy_count(favorites):
    # return a dictionary of candy names and the times it appears in friend favorite list
    # key should be name of candy, value should be number of times the candy appears in friend favorites.
    # create a new return dictonary
    # loop through favorites  to get the friends, then candy from the list
    # add counter of the amount of times a specific candy gets made
    fav_candy_count = {}
    # count = 0
    # print(favorites)
    for friends in favorites:
        # print(friends)
        for candy in friends[1]:
            # print(candy)
            if candy not in fav_candy_count:
                fav_candy_count[candy] = 1
            else:
                fav_candy_count[candy] += 1

        # for candies in friends:
        # print(candies[1])
    # print(fav_candy_count)
    return fav_candy_count
    # pass


def create_new_candy_data_structure(data):
    pass


def get_friends_who_like_specific_candy(data, candy_name):
    pass


def create_candy_set(data):
    pass


favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy"]],
    ["Bob", ["milky way", "licorice", "lollipop"]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
]
print(get_friends_favorite_candy_count(favorites))
