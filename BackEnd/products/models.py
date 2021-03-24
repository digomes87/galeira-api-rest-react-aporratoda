from django.db import models


class Category(model.Models):
  name = models.Charfield(max_length=250)

  def __str__(self):
    return self.name


class Seller(model.Models):
  name = models.Charfield(max_length=250)

  def __str__(self):
    return self.name
