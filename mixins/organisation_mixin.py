from django.db import models


class OrganisationMixin(models.Model):
    """
    This mixin adds the organisation field to the model
    """

    organisation = models.CharField(
        max_length=127,
    )

    class Meta:
        """
        Meta class for OrganisationMixin
        """

        abstract = True
