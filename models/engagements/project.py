import swapper
from django.db import models

from common_biodata.models.engagements.project import AbstractProject
from faculty_biodata.constants.project_types import PROJECT_TYPES
from faculty_biodata.models.abstract_classes.base_model import BaseModel
from formula_one.utils.upload_to import UploadTo


class Project(AbstractProject, BaseModel):
    """
    This model contains the projects undertaken by the faculty member
    """

    image = models.ImageField(
        upload_to=UploadTo('faculty_biodata', 'projects'),
        blank=True,
        null=True,
    )

    financial_outlay = models.CharField(
        max_length=127,
    )

    funding_agency = models.CharField(
        max_length=127,
    )

    other_investigating_officers = models.CharField(
        max_length=127,
        blank=True,
        null=True,
    )

    project_type = models.CharField(
        max_length=3,
        choices=PROJECT_TYPES,
    )

    class Meta:
        """
        Meta class for Project
        """

        swappable = swapper.swappable_setting('faculty_biodata', 'Project')

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        string = super().__str__()
        return f'{faculty_member} : {string}'
