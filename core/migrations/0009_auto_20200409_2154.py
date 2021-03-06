# Generated by Django 3.0.4 on 2020-04-10 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_movmensalista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensalista',
            name='veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo'),
        ),
        migrations.AlterField(
            model_name='movmensalista',
            name='mensalista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Mensalista'),
        ),
        migrations.AlterField(
            model_name='movrotativo',
            name='veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Marca'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='proprietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa'),
        ),
    ]
