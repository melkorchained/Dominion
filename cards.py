
class Card(object):
    """
    Represents a card class
    """

    def __init__(self, name, cost, treasure=False, victory=False, action=False, isReaction=False, isAttack=False, actions=0, cards=0, buys=0, treasures=0, victory_points=0, active=()):
        self.name = name
        self.cost = cost
        self.victory = victory
        self.treasure = treasure
        self.action = action
        self.reaction = isReaction
        self.attack = isAttack

# Define Card actives

def artisan_active():
    return

def bandit_active():
    return

def bureaucrat_active():
    return

def cellar_active():
    return

def chapel_active():
    return

def councilroom_active():
    return

def gardens_active():
    return

def harbinger_active():
    return

def library_active():
    return

def merchant_active():
    return

def militia_active():
    return

def mine_active():
    return

def moat_active():
    return

def moneylender_active():
    return

def poacher_active()L
    return

def remodel_active():
    return

def sentry_active():
    return

def throneroom_active():
    return

def vassal_active():
    return

def witch_active():
    return

def workshop_active():
    return()

# Define base cards

copper = Card('Copper', 0, treasure=True, treasures=1)
silver = Card('Silver', 3, treasure=True, treasures=2)
gold = Card('Gold', 6, treasure=True, treasures=3)
estate = Card('Estate', 2, victory=True, victory_points=2)
duchy = Card('Duchy', 5, victory=True, victory_points=3)
province = Card('Province', 8, victory=True, victory_points=6)
curse = Card('Curse', 0, victory=True, victory_points=-1)

base_cards = [copper, silver, gold, estate, duchy, province, curse]

# Define all other cards

artisan = Card('Artisan', 6, action=True, active=artisan_active())
bandit = Card('Bandit', 5, action=True, isAttack=True, active=bandit_active())
bureaucrat = Card('Bureaucrat', 4, action=True, isAttack=True, active=bureaucrat_active())
cellar = Card('Cellar', 2, action=True, actions=1, active=cellar_active())
chapel = Card('Chapel', 2, action=True, active=chapel_active())
council_room = Card('Council Room', 4, action=True, cards=4, buys=1, active=councilroom_active())
festival = Card('Festival', 5, action=True, actions=2, buys=1, treasures=2)
gardens = Card('Gardens', 4, victory=True, active=gardens_active())
harbinger = Card('Harbinger', 3, action=True, actions=1, cards=1, active=harbinger_active())
laboratory = Card('Laboratory', 5, action=True, actions=1, cards=2)
library = Card('Library', 5, action=True, active=library_active())
market = Card('Market', 5, action=True, actions=1, cards=1, buys=1, treasures=1)
merchant = Card('Merchant', 3, action=True, actions=1, cards=1, treasures=1, active=merchant_active())
militia = Card('Militia', 4, action=True, isAttack=True, treasures=2, active=militia_active())
mine = Card('Mine', 5, action=True, active=mine_active())
moat = Card('Moat', 2, action=True, isReaction=True, cards=2, active=moat_active())
moneylender = Card('Moneylender', 4, action=True, active=moneylender_active())
poacher = Card('Poacher', 4, action=True, actions=1, cards=1, treasures=1, active=poacher_active())
remodel = Card('Remodel', 4, action=True, active=remodel_active())
sentry = Card('Sentry', 5, action=True, actions=1, cards=1, active=sentry_active())
smithy = Card('Smithy', 4, action=True, cards=3)
throne_room = Card('Throne Room', action=True, active=throneroom_active())
vassal = Card('Vassal', action=True, treasures=2, active=vassal_active())
village = Card('Village', action=True, actions=2, cards=1)
witch = Card('Witch', action=True, isAttack=True, cards=2, active=witch_active())
workshop = Card('Workshop', action=True, active=workshop_active())
