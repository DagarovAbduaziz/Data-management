from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    treatment_method = models.TextField()
    # image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    disease = models.CharField(max_length=100)  # ✅ This field must exist!
    eye_image_url = models.URLField()  

    def __str__(self):
        return self.name