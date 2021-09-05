from django.db import models
from object.models import *


class Act(models.model):
    object = models.ForeignKey(ObjectOfBuilding, on_delete=models.SET_NULL)