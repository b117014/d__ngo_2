# Generated by Django 2.2.12 on 2020-05-08 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flights', '0005_auto_20200506_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passengers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flight', models.ManyToManyField(blank=True, related_name='passenger', to='Flights.Flights')),
            ],
        ),
    ]
