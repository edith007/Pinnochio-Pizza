from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_final_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='final_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_fullfilled',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_placed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
