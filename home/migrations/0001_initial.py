# Generated by Django 2.2.1 on 2019-08-24 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sondage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('date_publication', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choix', models.CharField(max_length=200)),
                ('nb_votes', models.IntegerField()),
                ('sondage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Sondage')),
            ],
        ),
    ]
