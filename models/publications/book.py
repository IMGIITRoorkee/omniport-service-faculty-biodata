import swapper

from common_biodata.models import AbstractBook
from faculty_biodata.models.abstract_classes.base_model import BaseModel


class Book(AbstractBook, BaseModel):
    """
    This model stores information about a book by a faculty member
    """

    class Meta:
        """
        Meta class for Book
        """

        swappable = swapper.swappable_setting('faculty_biodata', 'Book')

    def __str__(self):
        """
        Return a string representation of the model
        :return: a string representation of the model
        """

        faculty_member = self.faculty_member
        string = super().__str__()

        return f'{faculty_member} : {string}'
