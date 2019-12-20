import swapper
from django.contrib import admin

from omniport.admin.site import omnipotence

models = [
    'Profile',
    'Education',
    'Honour',
    'Visit',
    'Collaboration',
    'Project',
    'AssociateScholar',
    'Supervision',
    'TeachingEngagement',
    'Event',
    'Interest',
    'AdministrativePosition',
    'Membership',
    'Book',
    'Paper',
]

class BaseAdmin(admin.ModelAdmin):
    raw_id_fields = ('faculty_member',)

for model in models:
    omnipotence.register(
        swapper.load_model(
            'faculty_biodata', model
        ), BaseAdmin
    )
