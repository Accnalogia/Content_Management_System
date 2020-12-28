from django.core.management.base import BaseCommand
import random
from api.core.models import CMSUser

# python manage.py seed --mode=refresh

""" Clear all data and creates CMSUser """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    CMSUser.objects.all().delete()


def create_admin_user():
    """Creates an CMSUser object combining different elements from the list"""

    user = CMSUser.objects.create_user(username='jamesdoe@gmail.com', email='jamesdoe@gmail.com',
                                       password='qwerty12345', first_name='john',
                                       last_name='doe',
                                       phone_number='1548568289', pincode='145786', is_admin=True)

    return user

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    create_admin_user()
