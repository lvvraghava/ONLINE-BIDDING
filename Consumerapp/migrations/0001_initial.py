# Generated by Django 3.1.4 on 2021-01-11 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('prod_type', models.CharField(choices=[('Bricks', 'Bricks'), ('Sand', 'Sand'), ('Nails', 'Nails'), ('Screws', 'Screws'), ('Cement', 'Cement'), ('Glue', 'Glue'), ('Steel', 'Steel'), ('Paint', 'Paint'), (' ', ' ')], default=' ', max_length=10)),
                ('quantity', models.CharField(max_length=10)),
                ('high_value', models.DecimalField(decimal_places=2, max_digits=14)),
                ('bid_created_at', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('final_price', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('desc', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
