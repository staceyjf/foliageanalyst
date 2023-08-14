# Generated by Django 4.2.4 on 2023-08-14 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantCare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('water_amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('give_fertilizer', models.BooleanField()),
                ('fertilizer', models.CharField(choices=[('L', 'Liquid'), ('S', 'Slow release pellets'), ('N', 'N/A')], default='N', max_length=1)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.plants')),
            ],
        ),
    ]
