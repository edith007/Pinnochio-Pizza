from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190730_0216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='final_cost',
            new_name='total_cost',
        ),
    ]
