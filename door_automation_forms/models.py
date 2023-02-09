from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from jsignature.fields import JSignatureField


class Object(models.Model):
    """
    Model for the object (building)
    """
    class Meta:
        verbose_name = 'Objekt'
        verbose_name_plural = 'Objekt'

    name = models.CharField(
        max_length=254, verbose_name='Namn')
    address = models.TextField(
        max_length=500, null=True, blank=True, verbose_name='Adress')
    constructor = models.CharField(
        max_length=254, null=True, blank=True, verbose_name='Byggare')
    contact_person = models.CharField(
        max_length=254, null=True, blank=True, verbose_name='Kontaktperson')
    notes = models.TextField(
        max_length=500, blank=True, null=True, verbose_name='Anteckningar')
    drawing = models.FileField(
        null=True, blank=True, verbose_name='Ladda upp ritning',
        upload_to='uploads')
    date_created = models.DateTimeField(
        auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ControlChart(models.Model):
    """
    Model for the control chart
    """
    class Meta:
        verbose_name = 'Kontrollschema'
        verbose_name_plural = 'Kontrollscheman'

    DOOR_TYPE_CHOICES = [
        ('1-flyg', '1-flyg'),
        ('2-flyg', '2-flyg'),
    ]

    CHOICES = [
        ('OK', 'OK'),
        ('ANM', 'Anm.'),
        ('N/A', 'Ej aktuell'),
    ]

    object = models.ForeignKey('Object', on_delete=models.CASCADE)
    door_type = models.CharField(max_length=6, choices=DOOR_TYPE_CHOICES, verbose_name='Dörrtyp')
    position_id = models.CharField(max_length=14, verbose_name='Dörrposition/ID')
    done_by = models.CharField(max_length=54, verbose_name='Utfört av')
    date = models.DateField()

    doorframe = models.CharField(max_length=6, choices=CHOICES, verbose_name='1. Dörrkarm')
    door_leaves = models.CharField(max_length=6, choices=CHOICES, verbose_name='2. Dörrblad')
    threshold = models.CharField(max_length=6, choices=CHOICES, verbose_name='3. Tröskel')
    hinge = models.CharField(max_length=6, choices=CHOICES, verbose_name='4. Gångjärn')
    lock_chest = models.CharField(max_length=6, choices=CHOICES, verbose_name='5. Låskista')
    end_plate = models.CharField(max_length=6, choices=CHOICES, verbose_name='6. Slutbleck')
    edge_rule = models.CharField(max_length=6, choices=CHOICES, verbose_name='7. Kantregel')
    door_coordinator = models.CharField(max_length=6, choices=CHOICES, verbose_name='8. Dörrkoordinator')
    door_environment_clean = models.CharField(max_length=6, choices=CHOICES, verbose_name='9. Dörrmiljö rengjord')

    opener_attached_to_the_wall = models.CharField(max_length=6, choices=CHOICES, verbose_name='10. Öppnare riktigt fäst till vägg/parti')
    arm_system_attached = models.CharField(max_length=6, choices=CHOICES, verbose_name='11. Armsystem riktigt fäst till öppnare/dörr')
    arm_system_adjusted = models.CharField(max_length=6, choices=CHOICES, verbose_name='12. Armsystem riktigt justerat')
    cloosing_speed_adjusted1 = models.CharField(max_length=6, choices=CHOICES, verbose_name='13. Stängningshastighet riktigt justerat 1-flyg')
    closing_speed_adjusted2 = models.CharField(max_length=6, choices=CHOICES, verbose_name='14. Stängningshastighet riktigt justerat 2-flyg')
    opening_speed_adjusted1 = models.CharField(max_length=6, choices=CHOICES, verbose_name='15. Öppningshastighet riktigt justerat 1-flyg')
    opening_speed_adjusted2 = models.CharField(max_length=6, choices=CHOICES, verbose_name='16. Öppningshastighet riktigt justerat 2-flyg')
    opening_coordination = models.CharField(max_length=6, choices=CHOICES, verbose_name='17. Öppningskoordinering riktigt inställt 2-flyg')

    safety_sensor_tested = models.CharField(max_length=6, choices=CHOICES, verbose_name='18. Säkerhetssensor, justerad och testad')
    impulse_sensor_adjusted = models.CharField(max_length=6, choices=CHOICES, verbose_name='19. Impulsgivare (radar) riktigt monterat och justerat')
    control_signals_tested = models.CharField(max_length=6, choices=CHOICES, verbose_name='20. Styrsignaler från passersystem testat')
    fire_signals_tested = models.CharField(max_length=6, choices=CHOICES, verbose_name='21. Styrsignaler från brandlarm testat')

    notes = models.TextField(max_length=1000, verbose_name='Anmärkningar', help_text='Ange anmärkningar. Börja med siffran följt av notering. Ny anmärkning på ny rad.')

    signature = JSignatureField()

    def __str__(self):
        return self.position_id
