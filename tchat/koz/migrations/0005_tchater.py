# Generated by Django 3.0.7 on 2020-06-17 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('koz', '0004_delete_tchater'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tchater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField()),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profileTchat', to='koz.Profile')),
            ],
            options={
                'verbose_name': 'Tchater',
                'verbose_name_plural': 'Tchaters',
            },
        ),
    ]
