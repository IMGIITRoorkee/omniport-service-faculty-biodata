import swapper
from django.db import models

from common_biodata.models import AbstractInterest
from faculty_biodata.models.abstract_classes.base_model import BaseModel


class Interest(AbstractInterest, BaseModel):
    """
    This model contains the interests of the faculty member
    """

    class Meta:
        """
        Meta class for Interest
        """

        swappable = swapper.swappable_setting('faculty_biodata', 'Interest')

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        string = super().__str__()
        return f'{faculty_member}: {string}'
