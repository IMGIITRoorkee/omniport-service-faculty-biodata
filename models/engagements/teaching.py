import swapper
from django.db import models

from faculty_biodata.models.abstract_classes.base_model import BaseModel
from faculty_biodata.constants.semesters import SEMESTER_TYPES, SPRING


class AbstractTeachingEngagement(BaseModel):
    """
    This model contains the teaching engagements of the faculty member
    """

    class_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    
    student_count = models.IntegerField(
        blank=True
    )

    semester = models.CharField(
        blank=True,
    )
    course_title = models.CharField(
        max_length=127,
    )
    course_code = models.CharField(
        max_length=127,
    )
    class_name = models.CharField(
        max_length=127,
    )

    lecture_hours = models.IntegerField(
        blank=True,
    )
    practical_hours = models.IntegerField(
        blank=True,
    )
    tutorial_hours = models.IntegerField(
        blank=True,
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        course_title = self.course_title
        class_name = self.class_name
        return f'{faculty_member}: {course_title}, {class_name}'

    class Meta:
        """
        Meta class for AbstractTeachingEngagement
        """

        abstract = True


class TeachingEngagement(AbstractTeachingEngagement):
    """
    This class implements AbstractTeachingEngagement
    """

    semester = models.CharField(
        max_length=1,
        choices=SEMESTER_TYPES,
        default=SPRING,
    )

    class Meta:
        """
        Meta class for the TeachingEngagement
        """

        swappable = swapper.swappable_setting('faculty_biodata',
                                              'TeachingEngagement')
