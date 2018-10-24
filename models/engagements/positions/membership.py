import swapper

from common_biodata.models import AbstractPosition
from faculty_biodata.models.abstract_classes.base_model import BaseModel


class Membership(AbstractPosition, BaseModel):
    """
    This model contains information about a membership held by a faculty member
    """

    class Meta:
        """
        Meta class for Membership
        """

        swappable = swapper.swappable_setting('faculty_biodata', 'Membership')

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        string = super().__str__()
        return f'{faculty_member}: {string}'
