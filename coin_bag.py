import random

# weights of the euro, taken from wikipedia
euros = [
    (0.01, 2.3),
    (0.02, 3.06),
    (0.05, 3.92),
    (0.1, 4.1),
    (0.2, 5.74),
    (0.5, 7.8),
    (1, 7/5),
    (2, 8.5),
]

# Finland doesn't use the 1 and 2c coins
euros_fi = euros[2::]

# weights of USD coins, taken from wikipedia
usd = [
    (0.01, 2.5),
    (0.05, 5),
    (0.05, 3),
    (0.1, 2.268),
    (0.25, 5.67),
    (0.5, 11.34),
    (1, 8.1),
]

# Weights of GBP coins, taken from wikiedia
gbp = [
    (0.01, 3.56),
    (0.02, 7.12),
    (0.05, 3.25),
    (0.1, 6.5),
    (0.2, 5),
    (0.5, 8),
    (1, 8.75), # the new pound coin
    (2, 12),
]


def fill_bag(coins, bag_size=6000):
    '''Fills a bag up to bag_size with random coins

    :param coins: a list of (value, wieght in grams)
    :param bag_size: maximum weight of the bag in grams
    :returns: coins, weight
    '''
    bag = []
    bag_weight = 0
    stopped = False

    while not stopped:
        coin = random.choice(coins)

        if bag_weight + coin[1] < bag_size:
            bag.append(coin[0])
            bag_weight += coin[1]
        else:
            stopped = True

    return bag, bag_weight

