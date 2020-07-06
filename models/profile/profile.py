from django.db import models

import swapper
from formula_one.utils.upload_to import UploadTo

from common_biodata.models.profile.profile import AbstractProfile


class Profile(AbstractProfile):
    """
    This model constains informatation about the home page of the faculty_member
    """

    faculty_member = models.OneToOneField(
        to=swapper.get_model_name('kernel', 'FacultyMember'),
        on_delete=models.CASCADE,
    )
    resume = models.FileField(
        blank=True,
        null=True,
        upload_to=UploadTo('faculty_biodata', 'resume')
    )
    class Meta:
        """
        Meta class for AbstractProfile
        """

        swappable = swapper.swappable_setting('faculty_biodata', 'Profile')

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        string = super().__str__()
        return f'{faculty_member} : {string}'
