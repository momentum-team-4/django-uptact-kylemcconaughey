# Generated by Django 3.1.1 on 2020-09-20 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20200920_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='note',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.note'),
        ),
    ]
