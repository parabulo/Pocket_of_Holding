from django.db import models
import uuid
from django.contrib.auth.models import User

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField(max_length=50)
    host = models.OneToOneField(User, related_name="hosted_room", on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, related_name='rooms', on_delete=models.CASCADE)

class Participant(models.Model):
    user = models.ForeignKey(User, related_name='rooms', on_delete=models.CASCADE)
    room = models.ForeignKey(User, related_name='participants', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'room')