# from django.db import models

# Create your models here.


# class ProductDetail(models.Model):
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     title = models.CharField(max_length=20)
#     description = models.TextField(100)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     size = models.CharField(max_length=10)
#     quantity = models.IntegerField()
#     color = models.CharField(max_length=10)

#     def __str__(self):
#         return self.title