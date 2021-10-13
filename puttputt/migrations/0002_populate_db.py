# Generated by Django 3.1.6 on 2021-10-12 03:43

from django.db import migrations
from django.contrib.auth.models import User

# populates the puttputt app with its initial data
def populate_db(apps, schema_editor):
    # get the models
    Profile = apps.get_model('puttputt', 'Profile')
    SponsorInfo = apps.get_model('puttputt', 'SponsorInfo')
    Tournament = apps.get_model('puttputt', 'Tournament')
    PlayerInfo = apps.get_model('puttputt', 'PlayerInfo')
    ManagerInfo = apps.get_model('puttputt', 'ManagerInfo')
    DrinkInfo = apps.get_model('puttputt', 'DrinkInfo')
    LeaderBoard = apps.get_model('puttputt', 'LeaderBoard')
    Prizes = apps.get_model('puttputt', 'Prizes')
    DrinkOrder = apps.get_model('puttputt', 'DrinkOrder')
    VenueInfo = apps.get_model('puttputt', 'VenueInfo')

    manager = User.objects.create_user(username='manager', password='manager')
    manager.save()

    manager_profile = Profile(user=manager, profile_type='MAN')
    manager_profile.save()

    manager_info = ManagerInfo(profile=manager_profile, name='default manager', cash_on_hand=0)
    manager_info.save()

    # TODO: add the other info that needs to be in this population

class Migration(migrations.Migration):

    dependencies = [
        ('puttputt', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db),
    ]