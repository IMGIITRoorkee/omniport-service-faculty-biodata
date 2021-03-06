import swapper
from django.db import models
from tinymce.models import HTMLField

from faculty_biodata.models.abstract_classes.base_model import BaseModel

class AbstractMiscellaneous(BaseModel):
    """
    This model contains the miscellaneous things a Faculty member wants to add
    """

    heading = models.CharField(
        max_length=255,
    )

    description = HTMLField(
        blank=True,
    )

    class Meta:
        """
        Meta class for AbstractMiscellaneous
        """

        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        heading = self.heading
        return f'{faculty_member}: {heading}'


class Miscellaneous(AbstractMiscellaneous):
    """
    This class implements AbstractMiscellaneous
    """

    class Meta:
        """
        Meta class for Miscellaneous
        """

        swappable = swapper.swappable_setting('faculty_biodata', 'Miscellaneous')
        unique_together = ['faculty_member', 'heading']
        verbose_name_plural = 'miscellaneous'
