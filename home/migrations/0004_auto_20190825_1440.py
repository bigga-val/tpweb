# Generated by Django 2.2.1 on 2019-08-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190825_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reponse',
            name='nb_votes',
            field=models.CharField(max_length=11, null=True),
        ),
    ]