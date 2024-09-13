import swapper
from django.db import models

from common_biodata.models import AbstractPosition
from faculty_biodata.constants.scopes import SCOPES
from faculty_biodata.models.abstract_classes.base_model import BaseModel
from faculty_biodata.mixins.country_mixin import CountryMixin
from faculty_biodata.mixins.city_state_mixin import CityMixin, StateMixin


class AdministrativePosition(AbstractPosition, CountryMixin, CityMixin, StateMixin, BaseModel):
    """
    This model contains information about an administrative position held by a
    faculty member
    """

    scope = models.CharField(
        max_length=1,
        choices=SCOPES,
    )

    class Meta:
        """
        Meta class for AdministrativePosition
        """

        swappable = swapper.swappable_setting('faculty_biodata',
                                              'AdministrativePosition')

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        string = super().__str__()
        scope = self.get_scope_display()
        return f'{faculty_member}: {string} ({scope})'
