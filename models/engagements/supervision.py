import swapper
from django.db import models

from faculty_biodata.constants.supervision import SUPERVISION_CATEGORIES
from faculty_biodata.models.abstract_classes.base_model import BaseModel
from kernel.mixins.period_mixin import BlurryPeriodMixin


class AbstractSupervision(BlurryPeriodMixin, BaseModel):
    """
    This model contains the doctorates, projects and theses supervised by the
    faculty member
    """

    topic = models.CharField(
        max_length=255,
    )

    category = models.CharField(
        max_length=3,
        choices=SUPERVISION_CATEGORIES,
    )

    name_of_other_supervisors = models.TextField()

    scholars_name = models.TextField()

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

    class Meta:
        """
        Meta class for Supervision
        """

        swappable = swapper.swappable_setting('faculty_biodata', 'Supervision')
