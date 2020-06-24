import swapper
from django.db import models

from faculty_biodata.mixins.organisation_mixin import OrganisationMixin
from faculty_biodata.models.abstract_classes.base_model import BaseModel

from faculty_biodata.constants.collaboration_types import COLLABORATION_TYPES, OTHER

class AbstractCollaboration(OrganisationMixin, BaseModel):
    """
    This model contains the collaboration information of the faculty member
    """

    topic = models.CharField(
        max_length=255,
    )

    level = models.CharField(
        max_length=3,
        choices=COLLABORATION_TYPES,
        blank=True,
    )

    class Meta:
        """
        Meta class for AbstractCollaboration
        """

        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        topic = self.topic
        organisation = self.organisation
        return f'{faculty_member}: {topic}, {organisation}'


class Collaboration(AbstractCollaboration):
    """
    This class implements AbstractCollaboration
    """

    class Meta:
        """
        Meta class for Collaboration
        """

        swappable = swapper.swappable_setting('faculty_biodata',
                                              'Collaboration')
