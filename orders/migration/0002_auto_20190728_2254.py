from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='name',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='menusection',
            old_name='section',
            new_name='name',
        ),
    ]
