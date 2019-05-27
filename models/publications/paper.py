import swapper
from django.db import models

from common_biodata.models import AbstractPaper
from faculty_biodata.models.abstract_classes.base_model import BaseModel
from formula_one.utils.upload_to import UploadTo


class Paper(AbstractPaper, BaseModel):
    """
    This model stores information about a paper by a faculty member
    """

    file = models.FileField(
        upload_to=UploadTo('faculty_biodata', 'papers'),
        blank=True,
        null=True,
    )

    class Meta:
        """
        Meta class for Paper
        """

        swappable = swapper.swappable_setting('faculty_biodata', 'Paper')

    def __str__(self):
        """
        Return a string representation of the model
        :return: a string representation of the model
        """

        faculty_member = self.faculty_member
        string = super().__str__()

        return f'{faculty_member} : {string}'
