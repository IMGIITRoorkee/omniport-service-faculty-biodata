import swapper
from django.db import models

from faculty_biodata.mixins.organisation_mixin import OrganisationMixin
from faculty_biodata.models.abstract_classes.base_model import BaseModel
from faculty_biodata.mixins.country_mixin import CountryMixin
from faculty_biodata.mixins.city_state_mixin import CityMixin


class AbstractHonour(OrganisationMixin, CountryMixin, CityMixin, BaseModel):
    """
    This model holds the honours awarded to the faculty member
    """

    place_of_award = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    award = models.CharField(
        max_length=255,
    )

    year = models.IntegerField()

    class Meta:
        """
        Meta class for AbstractHonour
        """

        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        award = self.award
        return f'{faculty_member}: {award}'


class Honour(AbstractHonour):
    """
    This class implements AbstractHonour
    """

    class Meta:
        """
        Meta class for Honour
        """

        swappable = swapper.swappable_setting('faculty_biodata', 'Honour')
