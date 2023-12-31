# Generated by Django 4.2.5 on 2023-09-30 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='proj_img',
            field=models.ImageField(default=None, upload_to='img/<django.db.models.fields.CharField>/title/'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='img/None/content/'),
        ),
    ]
