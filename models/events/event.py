import swapper
from django.db import models

from faculty_biodata.constants.event_categories import EVENT_CATEGORIES
from faculty_biodata.constants.event_roles import EVENT_ROLES
from faculty_biodata.models.abstract_classes.base_model import BaseModel
from formula_one.mixins.period_mixin import PeriodMixin


class AbstractEvent(PeriodMixin, BaseModel):
    """
    This model contains information about any event
    """

    name = models.CharField(
        max_length=255,
    )

    sponsor = models.CharField(
        max_length=255,
        blank=True,
    )

    place = models.CharField(
        max_length=255,
    )

    category = models.CharField(
        max_length=3,
        choices=EVENT_CATEGORIES,
    )

    role = models.CharField(
        max_length=1,
        choices=EVENT_ROLES,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        """
        Meta class for BaseEvent
        """

        abstract = True

    def __str__(self):
        """
        Return a string representation of the model
        :return: a string representation of the model
        """

        faculty_member = self.faculty_member
        category = self.get_category_display()
        name = self.name
        return f'{faculty_member}: {name}, ({category})'


class Event(AbstractEvent):
    """
    This class implements AbstractEvent
    """

    class Meta:
        """
        Meta class for Event
        """

        swappable = swapper.swappable_setting('faculty_biodata', 'Event')
