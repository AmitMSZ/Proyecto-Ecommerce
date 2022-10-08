# Generated by Django 4.1.2 on 2022-10-06 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bodega",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=15)),
                ("locacion", models.CharField(max_length=15)),
            ],
            options={
                "db_table": "bodega",
            },
        ),
        migrations.CreateModel(
            name="Tipo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=20)),
                ("descripcion", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "tipo",
            },
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=20)),
                ("descripcion", models.CharField(max_length=130, null=True)),
                ("stock", models.IntegerField()),
                (
                    "bodega",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="productos.bodega",
                    ),
                ),
                (
                    "tipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="productos.tipo"
                    ),
                ),
            ],
            options={
                "db_table": "productos",
            },
        ),
    ]