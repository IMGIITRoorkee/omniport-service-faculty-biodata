import swapper

from common_biodata.models.accomplishments.education import AbstractEducation
from faculty_biodata.models.abstract_classes.base_model import BaseModel


class Education(AbstractEducation, BaseModel):
    """
    This model contains information about the education of a faculty member
    """

    class Meta:
        """
        Meta class for AbstractEducation
        """

        verbose_name_plural = 'education'
        swappable = swapper.swappable_setting('faculty_biodata', 'Education')

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        faculty_member = self.faculty_member
        string = super().__str__()
        return f'{faculty_member} : {string}'
