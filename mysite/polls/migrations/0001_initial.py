# Generated by Django 4.0.2 on 2022-02-08 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Magasin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(choices=[('BN', 'BENIN'), ('BF', 'BURKINA FASO'), ('CI', 'COTE D IVOIRE'), ('SN', 'SENEGAL')], max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('M', 'MASCULIN'), ('F', 'FEMININ'), ('NB', 'NON BINAIRE')], max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileMagasin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('phone', models.CharField(max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('magasin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='magasin_profile', to='polls.magasin')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(choices=[('BN', 'BENIN'), ('BF', 'BURKINA FASO'), ('CI', 'COTE D IVOIRE'), ('SN', 'SENEGAL')], max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='PRODUCT_IMG')),
                ('magasin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produit_magasin', to='polls.magasin')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
    ]
