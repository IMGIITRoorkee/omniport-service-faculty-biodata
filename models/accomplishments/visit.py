import swapper
from django.db import models

from faculty_biodata.models.abstract_classes.base_model import BaseModel
from faculty_biodata.mixins.country_mixin import CountryMixin


class AbstractVisit(BaseModel, CountryMixin):
    """
    This model contains the visits by the faculty member
    """

    purpose = models.CharField(
        max_length=255,
    )

    place = models.CharField(
        max_length=255,
    )

    date = models.DateField(
        blank=True,
        null=True,
    )

    class Meta:
        """
        Meta class for AbstractVisit
        """

        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        place = self.place
        return f'{faculty_member}: {place}'


class Visit(AbstractVisit):
    """
    This class implements AbstractVisit
    """

    class Meta:
        """
        Meta class for Visit
        """

        swappable = swapper.swappable_setting('faculty_biodata', 'Visit')
