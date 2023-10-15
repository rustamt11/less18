# Generated by Django 4.2.6 on 2023-10-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_status', models.BooleanField(default=False)),
                ('purchase_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
