# Generated by Django 4.2.3 on 2023-09-05 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('value', models.CharField(max_length=100, verbose_name='Value')),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='about_us_videos/', verbose_name='Video')),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='about_us.aboutus', verbose_name='About us')),
            ],
            options={
                'verbose_name': 'About us video',
                'verbose_name_plural': 'About us videos',
            },
        ),
        migrations.CreateModel(
            name='AboutUsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_us_images/', verbose_name='Image')),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='about_us.aboutus', verbose_name='About us')),
            ],
            options={
                'verbose_name': 'About us image',
                'verbose_name_plural': 'About us images',
            },
        ),
    ]
