import swapper

from kernel.admin.site import omnipotence

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

for model in models:
    omnipotence.register(
        swapper.load_model(
            'faculty_biodata', model
        )
    )