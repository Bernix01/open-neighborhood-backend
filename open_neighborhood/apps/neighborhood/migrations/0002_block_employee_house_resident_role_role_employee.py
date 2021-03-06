# Generated by Django 3.0.8 on 2020-07-07 22:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('block_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(
                    default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(
                    primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=10)),
                ('home_address', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('person_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='neighborhood.Person')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('house_id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('block_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='neighborhood.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(
                    default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Role_employee',
            fields=[
                ('re_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('employee_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='neighborhood.Employee')),
                ('role_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='neighborhood.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('resident_id', models.AutoField(
                    primary_key=True, serialize=False)),
                ('landlord', models.BooleanField()),
                ('created_at', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('house_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='neighborhood.House')),
                ('person_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='neighborhood.Person')),
            ],
        ),
    ]
