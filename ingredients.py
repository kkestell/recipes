import json
import re
from functools import cache
from pathlib import Path

from inflector import Inflector, English


class IngredientSplitter(object):
    def __init__(self):
        self.amount_re = re.compile("^([0-9⅛⅓⅔¼½¾\. ]+)(.+)$")
        self.units = {
            'fluid ounces': 'fluid ounce',
            'fluid ounce': 'fluid ounce',
            'pieces': 'piece',
            'piece': 'piece',
            'ounces': 'ounce',
            'ounce': 'ounce',
            'oz': 'ounce',
            'cups': 'cup',
            'cup': 'cup',
            'dashes': 'dash',
            'dash': 'dash',
            'teaspoons': 'teaspoon',
            'teaspoon': 'teaspoon',
            'slices': 'slice',
            'slice': 'slice',
            'pints': 'pint',
            'pint': 'pine',
            'tbs.': 'tablespoon',
            'tbsp': 'tablespoon',
            'tablespoons': 'tablespoon',
            'tablespoon': 'tablespoon',
            'packages': 'package',
            'package': 'package',
            'pounds': 'pound',
            'pound': 'pound',
            'pinches': 'pinch',
            'pinch': 'pinch',
            'gallons': 'gallon',
            'gallon': 'gallon',
            'cans': 'can',
            'can': 'can',
            'quarts': 'quart',
            'quart': 'quart',
            'bottles': 'bottle',
            'bottle': 'bottle',
            'baskets': 'basket',
            'basket': 'basket',
            'envelopes': 'envelope',
            'envelope': 'envelope',
            'bulbs': 'bulb',
            'bulb': 'bulb',
            'stalks': 'stalk',
            'stalk': 'stalk',
            'sprigs': 'sprig',
            'sprig': 'sprig',
            'heads': 'head',
            'head': 'head',
            'bags': 'bag',
            'bag': 'bag',
            'sheets': 'sheet',
            'sheet': 'sheet',
            'jars': 'jar',
            'jar': 'jar',
            'bunches': 'bunch',
            'bunch': 'bunch',
            'ears': 'ears',
            'ear': 'ear',
            'cloves': 'clove',
            'clove': 'clove'
        }
        self.inflector = Inflector(English)

    def stem(self, val):
        val = re.sub('\(.+\)', '', val).strip()

        val = val.split(',')[0].strip()

        val = val.removesuffix('to taste').strip()
        val = val.removesuffix('to cover').strip()

        val = val.removeprefix('whole').strip()
        val = val.removeprefix('ground').strip()
        val = val.removeprefix('freshly').strip()
        val = val.removeprefix('fresh').strip()
        val = val.removeprefix('very hot').strip()
        val = val.removeprefix('very warm').strip()
        val = val.removeprefix('small').strip()
        val = val.removeprefix('medium').strip()
        val = val.removeprefix('large').strip()
        val = val.removeprefix('warm').strip()
        val = val.removeprefix('cold').strip()
        val = val.removeprefix('good').strip()
        val = val.removeprefix('loosely').strip()

        val = val.replace('thick-cut', '').strip()
        val = val.replace('thick cut', '').strip()
        val = val.replace('thick', '').strip()
        val = val.replace('thin', '').strip()
        val = val.replace('slices', '').strip()
        val = val.replace('dozen', '').strip()

        val = val.replace('finely', '').strip()
        val = val.replace('coarsely', '').strip()

        val = val.replace('peeled', '').strip()
        val = val.replace('chopped', '').strip()
        val = val.replace('diced', '').strip()
        val = val.replace('minced', '').strip()
        val = val.replace('mashed', '').strip()
        val = val.replace('grated', '').strip()
        val = val.replace('blanched', '').strip()
        val = val.replace('sliced', '').strip()
        val = val.replace('cooked', '').strip()
        val = val.replace('cubed', '').strip()
        val = val.replace('drained', '').strip()
        val = val.replace('dried', '').strip()
        val = val.replace('dry', '').strip()
        val = val.replace('frozen', '').strip()
        val = val.replace('packed', '').strip()
        val = val.replace('firm', '').strip()

        val = re.sub('\s+', ' ', val).strip()

        # val = self.inflector.singularize(val)

        return val

    def amount(self, val):
        match = self.amount_re.match(val)
        if not match:
            return None

        return match.group(1).strip()

    def unit(self, val):
        val = re.sub('\(.+\)', '', val).strip()
        for unit in self.units.keys():
            if val.startswith(unit):
                return val.removeprefix(unit).strip(), self.units[unit]
        return val, 'ea'

    def normalize_fractions(self, val):
        val = val.replace('0.75', '¾')
        val = val.replace('0.5', '½')
        val = val.replace('1.5', '1 ½')

        val = val.replace('1/4', '¼')
        val = val.replace('1/2', '½')
        val = val.replace('3/4', '¾')
        val = val.replace('1/7', '⅐')
        val = val.replace('1/9', '⅑')
        val = val.replace('1/10', '⅒')
        val = val.replace('1/3', '⅓')
        val = val.replace('2/3', '⅔')
        val = val.replace('1/5', '⅕')
        val = val.replace('2/5', '⅖')
        val = val.replace('3/5', '⅗')
        val = val.replace('4/5', '⅘')
        val = val.replace('1/6', '⅙')
        val = val.replace('5/6', '⅚')
        val = val.replace('1/8', '⅛')
        val = val.replace('3/8', '⅜')
        val = val.replace('5/8', '⅝')
        val = val.replace('7/8', '⅞')

        return val

    @cache
    def split(self, ingredient):
        orig = self.normalize_fractions(ingredient)
        orig = orig.replace('\u2009', ' ')
        orig = orig.replace('.', '')
        orig = orig.strip()

        amount = self.amount(orig)

        if not amount:
            return None, None, None, None

        without_amount = orig.removeprefix(amount).strip().lower()
        without_unit, unit = self.unit(without_amount)

        stem = self.stem(without_unit)

        return amount.strip(), unit.strip(), orig, stem.strip()


if __name__ == '__main__':
    files = list(Path('./allrecipes_recipes/').glob('**/*.json'))
    all_ingredients = []
    for f in files:
        with open(f, 'r') as rfp:
            try:
                recipe_json = json.loads(rfp.read())
                for i in recipe_json['ingredients']:
                    all_ingredients.append(i)
            except:
                pass

    all_ingredients = list(set(all_ingredients))

    s = IngredientSplitter()

    stems = []
    for i in all_ingredients:
        i = i.replace('\t', ' ')
        i = re.sub('\s+', ' ', i).strip()
        _, _, _, stemmed = s.split(i)
        if stemmed:
            stems.append(stemmed)

    with open('stems.txt', 'w') as fp:
        for s in stems:
            fp.write(f"{s}\n")
