# Generated by Django 5.1.4 on 2024-12-23 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_convite_noiva_convite_noivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagina_login', models.ImageField(upload_to='')),
                ('pagina_inicial', models.ImageField(upload_to='')),
                ('pagina_perfil', models.ImageField(upload_to='')),
                ('noivos', models.ImageField(upload_to='')),
                ('pagina_confirm_1', models.ImageField(upload_to='')),
                ('pagina_confirm_2', models.ImageField(upload_to='')),
                ('pagina_confirm_3', models.ImageField(upload_to='')),
            ],
        ),
    ]
