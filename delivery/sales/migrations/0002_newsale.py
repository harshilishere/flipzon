# Generated by Django 3.2.9 on 2021-11-19 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.IntegerField()),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_add', models.CharField(max_length=500)),
                ('dod', models.IntegerField()),
                ('items_category', models.CharField(max_length=20)),
                ('items_qty', models.IntegerField()),
            ],
        ),
    ]
