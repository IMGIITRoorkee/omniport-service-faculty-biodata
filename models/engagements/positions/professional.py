import swapper
from django.db import models

from common_biodata.models import AbstractPosition
from faculty_biodata.models.abstract_classes.base_model import BaseModel
from faculty_biodata.mixins.country_mixin import CountryMixin
from faculty_biodata.mixins.city_state_mixin import CityMixin, StateMixin


class ProfessionalBackground(AbstractPosition, CountryMixin, CityMixin, StateMixin, BaseModel):
    """
    This model contains information about professional background of a
    faculty member
    """

    class Meta:
        """
        Meta class for ProfessionalBackground
        """

        swappable = swapper.swappable_setting('faculty_biodata','ProfessionalBackground')

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        string = super().__str__()
        return f'{faculty_member}: {string}'
