import swapper
from django.db import models

from formula_one.models.base import Model


class BaseModel(Model):
    """
    This abstract model contains the common fields of models
    """

    faculty_member = models.ForeignKey(
        to=swapper.get_model_name('kernel', 'FacultyMember'),
        on_delete=models.CASCADE,
    )

    priority = models.IntegerField(
        default=0,
    )

    visibility = models.BooleanField(
        default=True,
    )

    class Meta:
        """
        Meta class for BaseModel
        """

        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        return f'{faculty_member}'
