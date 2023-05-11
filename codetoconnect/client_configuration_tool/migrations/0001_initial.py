# Generated by Django 4.2.1 on 2023-05-11 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientConfigurations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('commisionTolerance', models.FloatField()),
                ('grossAmountTolerance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('roleId', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('roleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='client_configuration_tool.roles')),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('requestTime', models.DateTimeField()),
                ('grossAmountToleranceTo', models.FloatField()),
                ('commisionToleanceTo', models.FloatField()),
                ('clientConfigId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='client_configuration_tool.clientconfigurations')),
                ('requesterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester_requests', to='client_configuration_tool.users')),
                ('verifierId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verifier_requests', to='client_configuration_tool.users')),
            ],
        ),
        migrations.CreateModel(
            name='AuditLogs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField()),
                ('statusId', models.IntegerField()),
                ('grossAmountToleranceFrom', models.FloatField()),
                ('grossAmountToleranceTo', models.FloatField()),
                ('commisionToleranceFrom', models.FloatField()),
                ('commisionToleanceTo', models.FloatField()),
                ('clientConfigId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audit_logs', to='client_configuration_tool.clientconfigurations')),
                ('requestId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audit_logs', to='client_configuration_tool.requests')),
                ('requesterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester_audit_logs', to='client_configuration_tool.users')),
                ('verifierId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verifier_audit_logs', to='client_configuration_tool.users')),
            ],
        ),
    ]
