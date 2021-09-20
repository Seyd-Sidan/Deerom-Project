from django.db import models

# Create your models here.

class player(models.Model):
	player_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=20)
	email=models.EmailField(max_length=254)
	country=models.CharField(max_length=20)
	no_of_games=models.CharField(max_length=50)
	tot_score=models.IntegerField()

