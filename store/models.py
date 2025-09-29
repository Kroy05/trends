from django.db import models

class Store(models.Model):
    item_title= models.CharField(max_length=200)
    item_discrption= models.CharField(max_length=300)
    item_image= models.CharField(max_length=500, default="https://idacademyonline.com/wp-content/uploads/2019/01/Image-Coming-Soon-ECC.png")
    item_price= models.IntegerField()
    item_qty=models.IntegerField()
    item_color=models.CharField(max_length=50)
    item_fabric=models.CharField(max_length=100)
    item_Stiching=models.CharField(max_length=100)
    item_image2= models.CharField(max_length=500, default="https://idacademyonline.com/wp-content/uploads/2019/01/Image-Coming-Soon-ECC.png")
    item_image3= models.CharField(max_length=500, default="https://idacademyonline.com/wp-content/uploads/2019/01/Image-Coming-Soon-ECC.png")
    item_image4= models.CharField(max_length=500, default="https://idacademyonline.com/wp-content/uploads/2019/01/Image-Coming-Soon-ECC.png")
    


# Create your models here.
