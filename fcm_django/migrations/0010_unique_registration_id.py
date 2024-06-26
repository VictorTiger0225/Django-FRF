# Generated by Django 3.2.12 on 2022-03-31 11:10

from django.db import migrations, models

from fcm_django.settings import FCM_DJANGO_SETTINGS as SETTINGS

_MYSQL = "mysql"


class AlterFieldSkipMySQL(migrations.AlterField):
    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        if schema_editor.connection.vendor == _MYSQL:
            return
        super().database_forwards(
            app_label=app_label,
            schema_editor=schema_editor,
            from_state=from_state,
            to_state=to_state,
        )

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        if schema_editor.connection.vendor == _MYSQL:
            return
        super().database_backwards(
            app_label=app_label,
            schema_editor=schema_editor,
            from_state=from_state,
            to_state=to_state,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("fcm_django", "0009_alter_fcmdevice_user"),
    ]

    operations = (
        [
            AlterFieldSkipMySQL(
                model_name="fcmdevice",
                name="registration_id",
                field=models.TextField(
                    verbose_name="Registration token",
                    unique=True,
                ),
            ),
        ]
        if not SETTINGS["MYSQL_COMPATIBILITY"]
        else []
    )
