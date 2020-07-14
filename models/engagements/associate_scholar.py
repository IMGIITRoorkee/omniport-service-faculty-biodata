import swapper
from django.db import models

from faculty_biodata.models.abstract_classes.base_model import BaseModel


class AbstractAssociateScholar(BaseModel):
    """
    This model contains a research scholar associated with the faculty member
    """

    scholar_name = models.CharField(
        max_length=63,
    )
    institution = models.CharField(
        max_length=127,
    )
    home_page = models.URLField(
        blank=True,
        max_length=255,
    )
    interest = models.CharField(
        max_length=255,
    )

    class Meta:
        """
        Meta class for AbstractAssociateScholar
        """

        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        scholar_name = self.scholar_name
        return f'{faculty_member} - {scholar_name}'


class AssociateScholar(AbstractAssociateScholar):
    """
    This class implements AbstractAssociateScholar
    """

    class Meta:
        """
        Meta class for AssociateScholar
        """

        swappable = swapper.swappable_setting('faculty_biodata',
                                              'AssociateScholar')
