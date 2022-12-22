# Generated by Django 4.1.4 on 2022-12-22 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('balance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('amount', models.FloatField()),
                ('balance', models.FloatField()),
                ('date', models.CharField(max_length=20)),
                ('to', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expense_track.user')),
            ],
        ),
    ]