from django.db import models
import os

class Document(models.Model):
    attached = models.FileField('첨부 파일', upload_to="")

    def get_filename(self):
        return os.path.basename(self.attached.name)