# Generated by Django 3.2.4 on 2021-07-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0003_auto_20210626_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(upload_to='Projects/images'),
        ),
    ]
