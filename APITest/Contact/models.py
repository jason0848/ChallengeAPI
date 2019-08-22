from django.db import models


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=20, null=True)
    lastName = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.email}"

    class Meta:
        ordering = ['lastName']
