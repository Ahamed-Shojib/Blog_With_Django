# Generated by Django 5.1.6 on 2025-03-04 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0002_blog_catagory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-comment_date',)},
        ),
    ]
