from django.db import models


class Object(models.Model):
    """
    Model for the object (building)
    """
    class Meta:
        verbose_name = 'Objekt'
        verbose_name_plural = 'Objekt'

    name = models.CharField(max_length=254, verbose_name='Namn')
    address = models.TextField(max_length=500, null=True, blank=True, verbose_name='Adress')
    constructor = models.CharField(max_length=254, null=True, blank=True, verbose_name='Byggare')
    contact_person = models.CharField(max_length=254, null=True, blank=True, verbose_name='Kontaktperson')
    notes = models.TextField(max_length=500, blank=True, null=True, verbose_name='Anteckningar')
    drawing = models.FileField(null=True, blank=True, verbose_name='Ladda upp ritning')

    def __str__(self):
        return self.name


# class ControlChart(models.Model):
#     """
#     Model for the control chart
#     """
#     class Meta:
#         verbose_name = 'Kontrollschema'
#         verbose_name_plural = 'Kontrollscheman'

#     object = models.ForeignKey('Object', on_delete=models.CASCADE)
