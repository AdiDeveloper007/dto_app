# Generated by Django 3.2.5 on 2021-07-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dto', '0005_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='queries',
            field=models.CharField(max_length=300, null=True),
        ),
    ]