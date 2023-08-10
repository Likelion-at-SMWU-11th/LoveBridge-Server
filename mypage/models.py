from django.db import models
import os

class Document(models.Model):
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    
    def get_filename(self):
        return os.path.basename(self.imgfile.name)