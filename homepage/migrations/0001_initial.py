# Generated by Django 4.2.3 on 2023-09-06 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_reg', models.CharField(max_length=100)),
                ('completed', models.IntegerField()),
                ('ongoing', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
    ]
