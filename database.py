from peewee import *


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('recipes.db')


class Recipe(BaseModel):
    url = TextField(unique=True)
    author = TextField()
    published_on = TextField()
    modified_on = TextField()
    title = TextField()
    description = TextField(null=True)
    rating_value = FloatField()
    rating_count = IntegerField()
    image_url = TextField(null=True)


class RecipeIngredient(BaseModel):
    recipe = ForeignKeyField(Recipe, backref='ingredients')
    value = TextField()


class RecipeInstruction(BaseModel):
    recipe = ForeignKeyField(Recipe, backref='instructions')
    value = TextField()


class RecipeMeta(BaseModel):
    recipe = ForeignKeyField(Recipe, backref='meta')
    key = TextField()
    value = TextField()


class RecipeReview(BaseModel):
    recipe = ForeignKeyField(Recipe, backref='reviews')
    rating = IntegerField()
    author = TextField()
    body = TextField(null=True)
