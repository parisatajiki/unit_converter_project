from django.db import models

class Quantity(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Units(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.ForeignKey(Quantity, on_delete=models.SET_NULL, null=True ,related_name='units')

    def __str__(self):
        return self.title
