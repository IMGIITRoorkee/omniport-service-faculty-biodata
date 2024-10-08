import swapper
from django.db import models

from formula_one.mixins.period_mixin import BlurryPeriodMixin

from faculty_biodata.models.abstract_classes.base_model import BaseModel
from faculty_biodata.constants import supervision
from faculty_biodata.constants.phd_types import PHD_TYPES
from faculty_biodata.mixins.country_mixin import CountryMixin


class AbstractSupervision(BlurryPeriodMixin, CountryMixin, BaseModel):
    """
    This model contains the doctorates, projects and theses supervised by the
    faculty member
    """

    topic = models.CharField(
        max_length=255,
    )

    category = models.CharField(
        max_length=3,
        choices=supervision.SUPERVISION_CATEGORIES,
    )

    phd_type = models.CharField(
        blank=True,
    )

    name_of_other_supervisors = models.TextField(
        blank=True
    )

    scholars_name = models.TextField(
        blank=True
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        """
        Meta class for AbstractSupervision
        """

        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        topic = self.topic
        category = self.category
        return f'{faculty_member}: {topic} ({category})'


class Supervision(AbstractSupervision):
    """
    This class implements AbstractSupervision
    """

    phd_type = models.CharField(
        max_length=1,
        choices=PHD_TYPES,
        blank=True,
    )

    def save(self, *args, **kwargs):
        """
        Override save to ensure `phd_type` is blank when category is Project
        """

        if self.category == supervision.PROJECT:
            self.phd_type = ''
        super().save(*args, **kwargs)

    class Meta:
        """
        Meta class for Supervision
        """

        swappable = swapper.swappable_setting('faculty_biodata', 'Supervision')
