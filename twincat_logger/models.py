from django.db import models
from django.utils import timezone
from django.utils.http import int_to_base36
import uuid

ID_LENGTH=10
def id_gen() -> str:
    """Generates random string whose length is `ID_LENGTH`"""
    return int_to_base36(uuid.uuid4().int)[:ID_LENGTH]

class ProductionLine(models.Model):

    id = models.CharField(max_length=ID_LENGTH,primary_key=True,default=id_gen, verbose_name="ID")
    short_name = models.CharField(max_length=20, unique=True, verbose_name = "Short name", blank=False, null=False)
    long_name = models.CharField(max_length=255, verbose_name = "Long name")
    

    class Meta:
        ordering=["short_name"]
        verbose_name="Production line"
        verbose_name_plural = "Production lines"
    def __str__(self):
            return self.short_name
    

class LogData(models.Model):
    production_line = models.ForeignKey(ProductionLine,related_name='data', verbose_name="Production line",editable=True,on_delete=models.CASCADE)
    data_name = models.CharField(max_length=50, verbose_name = "Data name", blank=False, null=False)
    data_field = models.FloatField(verbose_name="Data field",default=None,editable=True, null=True, blank=True, )
    time_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Time of creation",editable=False)
    sender_ip = models.CharField(max_length=15, verbose_name = "Sender ip",default=None,editable=True, null=True, blank=True)

    class Meta:
        ordering=["time_of_creation"]
        verbose_name="Log data"
        verbose_name_plural = "Log data"
    def __str__(self):
            return f"DataLog entry[ Production line: {self.production_line.short_name}, Date+time: {str(self.time_of_creation)}, {self.data_name}: {self.data_field:.2f}"
    def __iter__(self):
         return iter([self.production_line,self.time_of_creation,self.data_field,self.sender_ip])
    

class LogMessage(models.Model):
    production_line = models.ForeignKey(ProductionLine,related_name='logmessage', verbose_name="Production line",editable=True,on_delete=models.CASCADE)
    CHOICES = (
        ('ALERT', 'Alert'),
        ('ERROR', 'Error'),
        ('PRODUCT_REJECTION', 'Product rejection')
    )
    message_type = models.CharField(max_length=50,default=CHOICES[0], verbose_name="Message type", choices = CHOICES, blank=False, null=False)
    message_text  = models.CharField(max_length=255, verbose_name = "Message text", blank=False, null=False,default="EMPTY")
    time_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Time of creation",editable=False)
    sender_ip = models.CharField(max_length=15, verbose_name = "Sender ip",default=None,editable=True, null=True, blank=True)

    def __str__(self):
         return f"Message from {self.production_line.short_name} : \"{self.message_type}: {self.message_text}\""
    
    class Meta:
        ordering=["time_of_creation"]
        verbose_name="Log message"
        verbose_name_plural = "Log messages"