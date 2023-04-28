from django.db import models
from db import BaseModel
class Question(BaseModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    class Meta(BaseModel.Meta):
        db_table = 'question'

class Choice(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    class Meta(BaseModel.Meta):
        db_table = 'choice'

class Place(BaseModel):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        db_table = 'place'

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    class Meta(Place.Meta):
        db_table = 'restaurant'

class Manager(BaseModel):
    name = models.CharField(max_length=128)
    age = models.IntegerField(null=True)
    restaurants = models.ManyToManyField(Restaurant)

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        db_table = 'manager'