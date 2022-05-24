import swapper

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
    'ProfessionalBackground',
    'Membership',
    'Book',
    'Paper',
    'Miscellaneous',
]

for model in models:
    omnipotence.register(
        swapper.load_model(
            'faculty_biodata', model
        )
    )
