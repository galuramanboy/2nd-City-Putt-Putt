# Generated by Django 3.2.7 on 2021-11-07 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('puttputt', '0005_auto_20211107_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managerinfo',
            name='cash_on_hand',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='playerinfo',
            name='current_hole',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='playerinfo',
            name='current_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='playerinfo',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='puttputt.tournament'),
        ),
    ]