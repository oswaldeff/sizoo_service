# Generated by Django 3.1.1 on 2020-09-17 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sizoo_proApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoesexp',
            old_name='shoesExp_shoe',
            new_name='ShoesExp_Shoe',
        ),
        migrations.RenameField(
            model_name='shoesexp',
            old_name='shoesExp_user',
            new_name='ShoesExp_User',
        ),
    ]
