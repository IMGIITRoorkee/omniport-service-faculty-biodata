from django.db import models




class CityMixin(models.Model):
    """
    This mixin adds the city field to the model
    """


    city = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )


    class Meta:
        """
        Meta class for CountryMixin
        """


        abstract = True

class StateMixin(models.Model):
    """
    This mixin adds the state field to the model
    """


    state = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )


    class Meta:
        """
        Meta class for CountryMixin
        """


        abstract = True



