# Generated by Django 2.2.1 on 2019-08-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190825_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reponse',
            name='nb_votes',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
