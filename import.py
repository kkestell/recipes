import functools
import json
import os
from pathlib import Path

from inflector import Inflector, English
from peewee import SqliteDatabase
from strsimpy.jaro_winkler import JaroWinkler

from ingredients import IngredientSplitter
from database import Recipe, RecipeIngredient, RecipeInstruction, RecipeMeta, RecipeReview

db = SqliteDatabase('recipes.db')

if os.path.exists('recipes.db'):
    os.remove('recipes.db')

db.connect()
db.create_tables([Recipe, RecipeIngredient, RecipeInstruction, RecipeMeta, RecipeReview])

# splitter = IngredientSplitter()

# ingredient_cache = {}

# inflector = Inflector(English)


# jarowinkler = JaroWinkler()


# @functools.cache
# def closest_ingredient(ingredient):
#     if ingredient in ingredient_cache:
#         return ingredient_cache[ingredient]
#
#     ci = None
#     cs = 0.0
#
#     for n, i in ingredient_cache.items():
#         score = jarowinkler.similarity(ingredient, n)
#         if score > cs:
#             cs = score
#             ci = i
#
#     # if cs < 0.9:
#     #     return None
#
#     return ci


# print('caching ingredients')
# with open('stems.txt', 'r') as fp:
#     print('reading file')
#     lines = [x.strip() for x in fp.readlines()]
#     total = len(lines)
#     cnt = 0
#     for s in lines:
#         cnt += 1
#         i, _ = Ingredient.get_or_create(name=s)
#         ingredient_cache[s] = i
#         print(f"{cnt}/{total} {s}")
#
#
#

# def find_or_create_ingredient(name):
#     if name not in ingredient_cache:
#         ing = Ingredient.create(name=name)
#         ingredient_cache[name] = ing
#         print(f"{name} not found in ingredient cache")
#     else:
#         print(name)
#     return ingredient_cache[name]

import re
from fractions import Fraction


def mixed_number(fraction: Fraction) -> str:
    whole = fraction.numerator // fraction.denominator
    remainder = fraction.numerator % fraction.denominator
    if whole == 0:
        return f"{fraction.numerator}/{fraction.denominator}"
    elif remainder == 0:
        return str(whole)
    else:
        return f"{whole} {remainder}/{fraction.denominator}"


def dec2frac(val):
    def yyy(match):
        d = match.groups(0)[0]
        f = mixed_number(Fraction(d).limit_denominator(8))
        return f
    foo = re.sub(r'([0-9]*\.?[0-9]+)', yyy, val)
    return foo


def frac2dec(val):
    def xxx(s):
        i, f = s.groups(0)
        f = Fraction(f)
        return str(int(i) + float(f))
    foo = re.sub(r'(?:(\d+)[-\s])?(\d+/\d+)', xxx, val)
    return foo


def normalize_fractions(val):
    return dec2frac(frac2dec(val))


print('importing recipes')
import_path = Path('./allrecipes_recipes/')
file_list = list(import_path.glob('**/*.json'))
cnt = 0
total = len(file_list)
for json_file in file_list:
    try:
        cnt += 1
        with json_file.open('rb') as jfp:
            recipe_json = json.loads(jfp.read().decode("utf-8"))
            if len(recipe_json.get('reviews', [])) < 20:
                continue
            if float(recipe_json.get('rating_value', 0.0)) < 4.5:
                continue
            recipe = Recipe.create(
                url=recipe_json['url'],
                author=recipe_json.get('author'),
                published_on=recipe_json['published_on'],
                modified_on=recipe_json['modified_on'],
                title=recipe_json['title'],
                description=recipe_json.get('description', None),
                rating_value=recipe_json.get('rating_value', 0.0) or 0.0,
                rating_count=recipe_json.get('rating_count', 0) or 0,
                image_url=recipe_json.get('image_url', None)
            )
            recipe.save()
            for i in recipe_json['ingredients']:
                i = normalize_fractions(i)
                recipe_ingredient = RecipeIngredient.create(recipe=recipe, value=i)
                recipe_ingredient.save()
            for i in recipe_json['instructions']:
                instruction = RecipeInstruction.create(recipe=recipe, value=i)
                instruction.save()
            for k, v in recipe_json.get('meta', {}).items():
                if not v:
                    continue
                meta = RecipeMeta.create(recipe=recipe, key=k, value=v)
                meta.save()
            for c in recipe_json['reviews']:
                if 'author' not in c or 'body' not in c:
                    continue
                if not c['author'] or not c['body']:
                    continue
                review = RecipeReview.create(
                    recipe=recipe,
                    rating=c['rating'],
                    author=c['author'],
                    body=c['body']
                )
                review.save()
            print(f"{cnt}/{total}")
    except Exception as e:
        print(e)