from django.db import models
from django.core.validators import MinValueValidator

class Campaign(models.Model):
    name = models.CharField(max_length=100)

class Player(models.Model):
    char_id = models.CharField(unique=True, max_length=8, primary_key=True)
    name = models.CharField(max_length=50)
    race = models.CharField(max_length=30)
    char_class = models.CharField(max_length=30)
    level = models.IntegerField()
    campaign = models.CharField(max_length=100)

    # Base Attributes
    strength = models.IntegerField(default=10, validators=[MinValueValidator(1)])
    dexterity = models.IntegerField(default=10, validators=[MinValueValidator(1)])
    constitution = models.IntegerField(default=10, validators=[MinValueValidator(1)])
    intelligence = models.IntegerField(default=10, validators=[MinValueValidator(1)])
    wisdom = models.IntegerField(default=10, validators=[MinValueValidator(1)])
    charisma = models.IntegerField(default=10, validators=[MinValueValidator(1)])

    # Proficiencies
    proficiency_choices = [('not_proficient', 'Not proficient'), ('proficient', 'Proficient'), ('expert', 'Expert')]

    athletics = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    acrobatics = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    stealth = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    sleight_of_hand = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    arcana = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    history = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    investigation = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    nature = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    religion = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    insight = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    animal_handling = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    medicine = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    perception = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    survival = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    performance = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    deception = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    intimidation = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')
    persuasion = models.CharField(max_length=20, choices=proficiency_choices, default='not_proficient')

    # Floating Statuses
    hit_points = models.IntegerField()
    armor_class = models.IntegerField()
    speed = models.FloatField(default=9.0)

class Ability(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    ability = models.CharField(max_length=30)
    description = models.TextField()

class InventoryItem(models.Model):
    name = models.CharField(max_length=40)
    item_type = models.CharField(max_length=20, choices=[('weapon', 'Weapon'),('armor', 'Armor'), ('consumable', 'Consumable'), ('misc', 'Miscellaneous')])
    weight = models.FloatField(default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='inventory')
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('player', 'item')