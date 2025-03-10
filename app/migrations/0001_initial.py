# Generated by Django 2.2.5 on 2019-11-13 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DogProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('product_type', models.TextField()),
                ('dog_size', models.TextField()),
                ('price', models.FloatField()),
                ('quanity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DogTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.TextField()),
                ('dog_name', models.TextField()),
                ('dog_birthdau', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_at', models.TimeField()),
                ('dog_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.DogProduct')),
            ],
        ),
    ]
