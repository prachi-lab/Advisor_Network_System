# Generated by Django 3.2.5 on 2021-07-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('advisor_name', models.CharField(blank=True, max_length=50, null=True)),
                ('advisor_id', models.IntegerField(blank=True, default='0', null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('export_to_CSV', models.BooleanField(default=False)),
            ],
        ),
    ]
