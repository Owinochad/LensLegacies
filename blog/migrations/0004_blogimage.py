# Generated by Django 4.2.6 on 2023-12-01 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('title', models.CharField(max_length=100)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]
