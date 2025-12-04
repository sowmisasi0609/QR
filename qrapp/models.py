from django.db import models

class PDFFile(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
    qr_image = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pdf)

