# Generated by Django 4.2.6 on 2023-10-26 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cocktailRecipes", "0003_alter_cocktailrecipe_ingredients_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200, verbose_name="Name")),
            ],
        ),
        migrations.RemoveField(
            model_name="cocktailrecipe",
            name="ingredients",
        ),
        migrations.AddField(
            model_name="cocktailrecipe",
            name="ingredients",
            field=models.ManyToManyField(related_name="cocktail_recipes", to="cocktailRecipes.ingredient"),
        ),
    ]