# Generated by Django 2.2.5 on 2019-09-30 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='importance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='position',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
