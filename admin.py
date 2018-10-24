import swapper

from kernel.admin.site import omnipotence

Education = swapper.load_model('faculty_biodata', 'Education')
Honor = swapper.load_model('faculty_biodata', 'Honor')
Visit = swapper.load_model('faculty_biodata', 'Visit')
Collaboration = swapper.load_model('faculty_biodata', 'Collaboration')
Project = swapper.load_model('faculty_biodata', 'Project')
AssociateScholar = swapper.load_model('faculty_biodata', 'AssociateScholar')
Supervision = swapper.load_model('faculty_biodata', 'Supervision')
TeachingEngagement = swapper.load_model(
    'faculty_biodata', 'TeachingEngagement')
Event = swapper.load_model('faculty_biodata', 'Event')
Interest = swapper.load_model('faculty_biodata', 'Interest')
AdministrativePosition = swapper.load_model(
    'faculty_biodata',
    'AdministrativePosition'
)
Membership = swapper.load_model('faculty_biodata', 'Membership')
# Book = swapper.load_model('faculty_biodata', 'Book')
# Paper = swapper.load_model('faculty_biodata', 'Paper')

omnipotence.register(Education)
omnipotence.register(Honor)
omnipotence.register(Visit)
omnipotence.register(Collaboration)
omnipotence.register(Project)
omnipotence.register(AssociateScholar)
omnipotence.register(Supervision)
omnipotence.register(TeachingEngagement)
omnipotence.register(Event)
omnipotence.register(Interest)
omnipotence.register(AdministrativePosition)
omnipotence.register(Membership)
# omnipotence.register(Book)
# omnipotence.register(Paper)
