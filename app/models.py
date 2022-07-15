from django.db import models

class Address(models.Model):
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField(default=0)

    def __str__(self):
        result = self.line1 + "\n"
        if self.line2 != "":
            result += self.line2 + "\n"
        result += self.city + ", " + self.state + " " + str(self.zipcode)
        return result

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name + "\n" + self.address

