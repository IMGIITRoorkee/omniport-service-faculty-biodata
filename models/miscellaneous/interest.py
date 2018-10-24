import swapper
from django.db import models

from common_biodata.models import AbstractInterest


class Interest(AbstractInterest):
    """
    This model contains the interests of the faculty member
    """

    faculty_member = models.OneToOneField(
        to=swapper.get_model_name('kernel', 'FacultyMember'),
        on_delete=models.CASCADE,
    )

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
