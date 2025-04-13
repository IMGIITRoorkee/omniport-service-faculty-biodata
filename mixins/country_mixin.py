from django.db import models
from faculty_biodata.constants.country import COUNTRIES




class CountryMixin(models.Model):
    """
    This mixin adds the country field to the model
    """


    country = models.CharField(
        max_length=127,
        choices=COUNTRIES,
        blank=False,
        
    )


    class Meta:
        """
        Meta class for CountryMixin
        """


        abstract = True



