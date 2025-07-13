from django.db import models

class PassportData(models.Model):
    """
    Model to store extracted passport data
    """
    # Image file
    image = models.ImageField(upload_to='passport_images/')
    
    # Extracted data fields
    passport_number = models.CharField(max_length=20, blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=50, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    issuing_authority = models.CharField(max_length=100, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Passport {self.passport_number} - {self.full_name}"
