from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_possible_toppings', models.IntegerField(blank=True, default=0)),
                ('price_per_additional_topping', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='MenuSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_placed', models.DateTimeField()),
                ('datetime_fullfilled', models.DateTimeField(blank=True, default=None)),
                ('status', models.CharField(choices=[('cart', 'Cart'), ('progress', 'In Progress'), ('oiw', "On it's Way")], default='cart', max_length=10)),
                ('items', models.ManyToManyField(related_name='cart', to='orders.CustomerItem')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='price',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='available_sizes',
            field=models.ManyToManyField(default='One-Size', to='orders.Size'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='available_topping_options',
            field=models.ManyToManyField(blank=True, related_name='selected_toppings', to='orders.Topping'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.MenuSection'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Item'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='prices',
            field=models.ManyToManyField(to='orders.Price'),
        ),
        migrations.AddField(
            model_name='customeritem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.MenuSection'),
        ),
        migrations.AddField(
            model_name='customeritem',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.MenuItem'),
        ),
        migrations.AddField(
            model_name='customeritem',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
        migrations.AddField(
            model_name='customeritem',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='orders.Topping'),
        ),
    ]
