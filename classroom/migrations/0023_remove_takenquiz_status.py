# Generated by Django 2.2.2 on 2019-07-03 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0022_auto_20190702_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='takenquiz',
            name='status',
        ),
    ]
