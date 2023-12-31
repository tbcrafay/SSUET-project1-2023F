from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    flat_number = models.IntegerField(default=0)  # Use CharField or PositiveIntegerField as appropriate
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    # Floor and room number
    floor_number = models.PositiveSmallIntegerField(default=1)
    room_number = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"Flat {self.flat_number}"




class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

