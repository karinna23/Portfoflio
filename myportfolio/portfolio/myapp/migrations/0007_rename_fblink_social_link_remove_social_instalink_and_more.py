# Generated by Django 4.0 on 2024-03-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_social_alter_about_image1_alter_about_image2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='social',
            old_name='fblink',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='social',
            name='instalink',
        ),
        migrations.RemoveField(
            model_name='social',
            name='tglink',
        ),
        migrations.RemoveField(
            model_name='social',
            name='xlink',
        ),
        migrations.AddField(
            model_name='social',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
