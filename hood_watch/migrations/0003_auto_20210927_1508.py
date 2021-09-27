# Generated by Django 3.2.7 on 2021-09-27 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood_watch', '0002_auto_20210927_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='hood',
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='name', max_length=20),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=20)),
                ('post_image', models.ImageField(blank=True, upload_to='images/posts')),
                ('content', models.TextField(blank=True, max_length=500)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood_watch.user')),
            ],
        ),
        migrations.CreateModel(
            name='Hood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hood_photo', models.ImageField(upload_to='images/hoods/')),
                ('name', models.CharField(default='name', max_length=100, null=True)),
                ('occupants_count', models.PositiveIntegerField(default=0)),
                ('police_contact', models.IntegerField(blank=True, default=0)),
                ('health_contact', models.IntegerField(blank=True, default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood_watch.user')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_pic', models.ImageField(blank=True, null=True, upload_to='images/business/')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('hood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood_watch.hood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood_watch.user')),
            ],
        ),
    ]
