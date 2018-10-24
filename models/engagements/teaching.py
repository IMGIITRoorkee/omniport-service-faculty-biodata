import swapper
from django.db import models

from faculty_biodata.models.abstract_classes.base_model import BaseModel


class AbstractTeachingEngagement(BaseModel):
    """
    This model contains the teaching engagements of the faculty member
    """

    class_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    student_count = models.IntegerField()

    course = models.CharField(
        max_length=127,
    )

    lecture_hours = models.IntegerField()
    practical_hours = models.IntegerField()
    tutorial_hours = models.IntegerField()

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        course = self.course
        class_name = self.class_name
        return f'{faculty_member}: {course}, {class_name}'

    class Meta:
        """
        Meta class for AbstractTeachingEngagement
        """

        abstract = True


class TeachingEngagement(AbstractTeachingEngagement):
    """
    This class implements AbstractTeachingEngagement
    """

    class Meta:
        """
        Meta class for the TeachingEngagement
        """

        swappable = swapper.swappable_setting('faculty_biodata',
                                              'TeachingEngagement')
