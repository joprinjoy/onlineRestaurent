# Generated by Django 3.2.7 on 2024-02-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurent', '0004_alter_menu_pdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='prtprice',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]