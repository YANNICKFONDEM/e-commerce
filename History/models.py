from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from django.conf import Settings
from django.contrib.auth.models import User

from . signals import object_viewed_signal

# Create your models here.

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True) # for the products
    object_id = models.PositiveIntegerField() # for the id of the products
    content_object = GenericForeignKey() # is the actual object
    viewed_on =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s Viewed: %s" %(self.content_object, self.viewed_on)
    
class Meta:
    verbose_name_lural = "Histories"
    
def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    if request.user.is_authenticated:
        new_history = History.objects.create(
            user = request.user,
            content_type = ContentType.objects.get_for_model(sender),
            object_id = instance.id,
            content_object=instance
        )
    
object_viewed_signal.connect(object_viewed_receiver)