from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


# Create your models here.

class Role(models.Model):
    ROLE_CHOICES = [
        ('prefect', 'Prefect'),
        ('class_leader', 'Class Leader'),
        ('cadet', 'Cadet'),
        ('first_aid', 'First Aid'),
        ('media_unit', 'Media Unit'),
        ('environmental_officer', 'Environmental Officer'),
        ('the_band', 'The Band'),
        ('others', 'Others')
    ]

    role_name = models.CharField(max_length=100, choices=ROLE_CHOICES)

    def __str__(self):
        return self.role_name

class Student(models.Model):
    student_id = models.CharField(max_length=100, null=False, blank=False)
    DOB = models.DateField(null=False, blank=False)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    address = models.TextField(max_length=100, null=False, blank=False)
    mother_full_name = models.CharField(max_length=100, null=False, blank=False)
    mother_job = models.CharField(max_length=100, null=False, blank=False)
    father_full_name = models.CharField(max_length=100, null=False, blank=False)
    father_job = models.CharField(max_length=100, null=False, blank=False)
    parent_contact_number = models.CharField(max_length=10,null=False, blank=False)
    whatsapp_number = models.CharField(max_length=10,null=False, blank=False)
    other_roles = models.ManyToManyField(Role, related_name='students', blank=True)
    have_siblings = models.BooleanField(null=False, blank=False)

    def clean(self):
        # Check if the date of birth is in the future
        if self.DOB and self.DOB > timezone.now().date():
            raise ValidationError("Date of birth cannot be in the future.")
        
    # def save(self, *args, **kwargs):
    #     if self.other_roles:
    #         self.other_roles = ','.join(self.other_roles)  # Saving multiple choices as comma-separated values
    #     super(Student, self).save(*args, **kwargs)
    
    # def get_other_role(self):
    #     if self.other_roles:
    #         return self.other_roles.split(',')  # Returning multiple choices as a list
    #     return []

    def __str__(self):
        return self.full_name
    

class Sibling(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='siblings')
    sibling_index_num = models.CharField(max_length=100)
    sibling_name = models.CharField(max_length=100)
    sibling_grade = models.IntegerField()

    def __str__(self):
        return self.sibling_name
    

class Achievement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='achievements')
    achievement_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)

    def __str__(self):
        return self.achievement_name
