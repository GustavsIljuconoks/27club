# Generated by Django 4.1.5 on 2023-03-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_remove_form_see_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='background_color',
            field=models.CharField(default='#f0f0f0', max_length=20),
        ),
        migrations.AlterField(
            model_name='form',
            name='confirmation_message',
            field=models.CharField(default='Jūsu atbilde ir iesniegta.', max_length=10000),
        ),
    ]
