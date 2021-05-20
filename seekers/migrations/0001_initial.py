# Generated by Django 3.2 on 2021-05-19 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seeker',
            fields=[
                ('base_user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    primary_key=True,
                    serialize=False,
                    to='users.user'
                    )),
                ('start_date', models.DateField()),
                ('min_rent', models.IntegerField()),
                ('max_rent', models.IntegerField()),
                ('num_of_roomates', models.IntegerField()),
                ('num_of_rooms', models.IntegerField()),
                ('about', models.TextField(blank=True)),
                ('city', models.ForeignKey(
                    on_delete=django.db.models.deletion.RESTRICT,
                    related_name='city_seekers',
                    to='apartments.city'
                    )),
            ],
        ),
    ]
