# Generated by Django 3.2.9 on 2021-11-19 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_newsale'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('model_no', models.CharField(max_length=20)),
                ('available', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='newsale',
            name='customer_add',
            field=models.CharField(default=' ', max_length=500),
        ),
        migrations.AlterField(
            model_name='newsale',
            name='dod',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newsale',
            name='items_category',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='newsale',
            name='items_qty',
            field=models.IntegerField(default=0),
        ),
    ]
