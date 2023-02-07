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

    object = models.ForeignKey('Object', on_delete=models.CASCADE)
    door_type = models.CharField(max_length=6, choices=DOOR_TYPE_CHOICES, verbose_name='Dörrtyp')
    position_id = models.CharField(max_length=14, verbose_name='Dörrposition/ID')
    done_by = models.CharField(max_length=54, verbose_name='Utfört av')
    date = models.DateField()

    doorframe = models.BooleanField(verbose_name='Dörrkarm')
    door_leaves = models.BooleanField(verbose_name='Dörrblad')
    threshold = models.BooleanField(verbose_name='Tröskel')
    hinge = models.BooleanField(verbose_name='Gångjärn')
    lock_chest = models.BooleanField(verbose_name='Låskista')
    end_plate = models.BooleanField(verbose_name='Slutbleck')
    edge_rule = models.BooleanField(verbose_name='Kantregel')
    door_coordinator = models.BooleanField(verbose_name='Dörrkoordinator')
    door_environment_clean = models.BooleanField(verbose_name='Dörrmiljö rengjord')

    opener_attached_to_the_wall = models.BooleanField(verbose_name='Öppnare riktigt fäst till vägg/parti')
    arm_system_attached = models.BooleanField(verbose_name='Armsystem riktigt fäst till öppnare/dörr')
    arm_system_adjusted = models.BooleanField(verbose_name='Armsystem riktigt justerat')
    cloosing_speed_adjusted1 = models.BooleanField(verbose_name='Stängningshastighet riktigt justerat 1-flyg')
    closing_speed_adjusted2 = models.BooleanField(verbose_name='Stängningshastighet riktigt justerat 2-flyg')
    opening_speed_adjusted1 = models.BooleanField(verbose_name='Öppningshastighet riktigt justerat 1-flyg')
    opening_speed_adjusted2 = models.BooleanField(verbose_name='Öppningshastighet riktigt justerat 2-flyg')
    opening_coordination = models.BooleanField(verbose_name='Öppningskoordinering riktigt inställt 2-flyg')

    safety_sensor_tested = models.BooleanField(verbose_name='Säkerhetssensor, justerad och testad')
    impulse_sensor_adjusted = models.BooleanField(verbose_name='Impulsgivare (radar) riktigt monterat och justerat')
    control_signals_tested = models.BooleanField(verbose_name='Styrsignaler från passersystem testat')
    fire_signals_tested = models.BooleanField(verbose_name='Styrsignaler från brandlarm testat')

    notes = models.TextField(max_length=1000, verbose_name='Anmärkningar', help_text='Ange anmärkningar till fälten som inte är ibockade ovan')

    signature = JSignatureField()

    def __str__(self):
        return self.position_id
