# Generated by Django 3.0.2 on 2020-01-26 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('available', models.BooleanField()),
                ('color', models.CharField(choices=[('WT', 'White'), ('YW', 'Yellow'), ('BK', 'Black'), ('RD', 'Red'), ('GN', 'Green'), ('PL', 'Purple')], max_length=5)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kfas.Author')),
            ],
        ),
    ]