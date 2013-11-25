from __future__ import division 
from fractions import Fraction
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

def convert(recipe=recipe, scale=1.0):
    "Convert a recipe, rescaling it as necessary"
    for ingredient, (amt, measurement) in recipe.items():
        amt = amt * scale
        if measurement == "cup":
            amt = amt*in_tbsp[measurement]
            measurement = 'tbsp'

        # if it's a whole number, print that, without trailing ".0"
        if int(amt) == amt:
            amt=int(amt)
        else:
            wholes = int(amt)
            parts = Fraction(amt-wholes)
            if wholes == 0:
                wholes=''
            else:
                wholes = str(wholes) + " "
            amt = wholes + str(parts)
        print amt, measurement, "of", ingredient


convert(recipe, 1/4) # added another 4 tsp of cocoa powder, 1/4 tsp vanilla

recipe_2 = recipe.copy()
recipe_2['sugar'] = [1, 'cup']
        
convert(recipe_2, 1/4)


