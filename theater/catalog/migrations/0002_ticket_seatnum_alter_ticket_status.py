# Generated by Django 4.2.2 on 2023-06-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='seatnum',
            field=models.PositiveIntegerField(default=123, help_text='Enter the number of seat'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.BooleanField(default=True, help_text='Specify if the ticket is available or sold', verbose_name='Available'),
        ),
    ]
