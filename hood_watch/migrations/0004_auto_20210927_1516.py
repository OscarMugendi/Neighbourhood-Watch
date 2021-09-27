# Generated by Django 3.2.7 on 2021-09-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood_watch', '0003_auto_20210927_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_pic',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='images/business/'),
        ),
        migrations.AlterField(
            model_name='business',
            name='description',
            field=models.TextField(blank=True, default='description', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.CharField(blank=True, default='email', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(blank=True, default='name', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hood',
            name='hood_photo',
            field=models.ImageField(default=0, upload_to='images/hoods/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, default='content', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, default=0, upload_to='images/posts'),
        ),
    ]
