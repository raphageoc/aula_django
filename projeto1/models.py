# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Africa(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    cntry_name = models.CharField(max_length=40, blank=True, null=True)
    count = models.BigIntegerField(blank=True, null=True)
    first_fips = models.CharField(max_length=2, blank=True, null=True)
    first_regi = models.CharField(max_length=21, blank=True, null=True)
    first_cont = models.CharField(max_length=13, blank=True, null=True)
    sum_pop_ad = models.FloatField(blank=True, null=True)
    sum_sqkm_a = models.FloatField(blank=True, null=True)
    sum_sqmi_a = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'africa'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Despesa(models.Model):

    class Meta:
        managed = False
        db_table = 'despesa'


class DespesasOriginal(models.Model):
    ano_empenho = models.TextField(blank=True, null=True)
    dt_empenho = models.TextField(blank=True, null=True)
    cd_fonte = models.TextField(blank=True, null=True)
    ds_fonte = models.TextField(blank=True, null=True)
    cd_funcao = models.TextField(blank=True, null=True)
    ds_funcao = models.TextField(blank=True, null=True)
    cd_programa = models.TextField(blank=True, null=True)
    ds_programa = models.TextField(blank=True, null=True)
    cd_acao = models.TextField(blank=True, null=True)
    ds_acao = models.TextField(blank=True, null=True)
    cd_subelemento = models.TextField(blank=True, null=True)
    ds_subelemento = models.TextField(blank=True, null=True)
    cd_orgao = models.TextField(blank=True, null=True)
    ds_orgao = models.TextField(blank=True, null=True)
    cd_despesa = models.TextField(blank=True, null=True)
    ds_despesa = models.TextField(blank=True, null=True)
    codigo_despesa_grupo = models.TextField(blank=True, null=True)
    ds_grupo = models.TextField(blank=True, null=True)
    codigo_despesa_modalidade = models.TextField(blank=True, null=True)
    ds_modalidade = models.TextField(blank=True, null=True)
    codigo_despesa_elemento = models.TextField(blank=True, null=True)
    ds_elemento = models.TextField(blank=True, null=True)
    cpf_cnpj = models.TextField(blank=True, null=True)
    nr_empenho = models.TextField(blank=True, null=True)
    licitacao = models.TextField(blank=True, null=True)
    vl_empenhado = models.TextField(blank=True, null=True)
    cd_item = models.TextField(blank=True, null=True)
    ds_item = models.TextField(blank=True, null=True)
    ds_unidade = models.TextField(blank=True, null=True)
    quantidade = models.TextField(blank=True, null=True)
    vl_preco_unitario = models.TextField(blank=True, null=True)
    vl_total = models.TextField(blank=True, null=True)
    protocolosup = models.TextField(blank=True, null=True)
    dt_transacao = models.TextField(blank=True, null=True)
    vl_liquidado = models.TextField(blank=True, null=True)
    vl_devolvido = models.TextField(blank=True, null=True)
    vl_anulado = models.TextField(blank=True, null=True)
    vl_pago = models.TextField(blank=True, null=True)
    vl_consignado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'despesas_original'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'
