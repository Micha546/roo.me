# Generated by Django 3.2 on 2021-04-24 19:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apartments', '0002_auto_20210422_0602'),
        ('users', '0006_test_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('date_created', models.DateField(default=datetime.date.today)),
                ('apartment', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='apt_connection',
                    to='apartments.apartment')),
                ('seeker', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='seeker_connection',
                    to='users.seeker')),
            ],
            options={
                'unique_together': {('apartment', 'seeker')},
            },
        ),
    ]
