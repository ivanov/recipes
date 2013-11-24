from __future__ import division 
in_tbsp = dict(cup=16)
in_tsp = dict(tbsp=3)
in_cups = dict()

# makes 10-15 mocha lattes (1 cup of chocolate syrup)
recipe = dict(
        cocoa_powder = [1/4, 'cup'],
        sugar = [3/8, 'cup'],
        salt = [1, 'dash'],
        water = [1/2, 'cup'],
        vanilla = [1, 'tsp']
        )

def convert(scale=1.0):
    for ingredient, (amt, measurement) in recipe.items():
        amt = amt * scale
        if measurement == "cup":
            amt = amt*in_tbsp[measurement]
            measurement = 'tbsp'
        print amt, measurement, "of", ingredient


convert(1/4)
        


