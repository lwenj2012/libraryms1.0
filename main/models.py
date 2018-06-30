# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class TbBookcase(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    column_3 = models.CharField(db_column='Column_3', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_bookcase'


class TbBookinfo(models.Model):
    barcode = models.CharField(max_length=30, blank=True, null=True)
    bookname = models.CharField(max_length=70, blank=True, null=True)
    typeid = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    translator = models.CharField(max_length=30, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    bookcase = models.IntegerField(blank=True, null=True)
    intime = models.DateField(db_column='inTime', blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(max_length=30, blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'tb_bookinfo'


class TbBooktype(models.Model):
    typename = models.CharField(max_length=30, blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_booktype'


class TbBorrow(models.Model):
    readerid = models.IntegerField(blank=True, null=True)
    bookid = models.IntegerField(blank=True, null=True)
    borrowtime = models.DateField(db_column='borrowTime', blank=True, null=True)  # Field name made lowercase.
    backtime = models.DateField(db_column='backTime', blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(max_length=30, blank=True, null=True)
    ifback = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_borrow'


class TbGiveback(models.Model):
    readerid = models.IntegerField(blank=True, null=True)
    bookid = models.IntegerField(blank=True, null=True)
    backtime = models.DateField(db_column='backTime', blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_giveback'


class TbLibrary(models.Model):
    libraryname = models.CharField(max_length=50, blank=True, null=True)
    curator = models.CharField(max_length=10, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    createdate = models.DateField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    introduce = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_library'


class TbManager(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    pwd = models.CharField(db_column='PWD', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_manager'


class TbParameter(models.Model):
    cost = models.IntegerField(blank=True, null=True)
    validity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_parameter'


class TbPublishing(models.Model):
    isbn = models.CharField(db_column='ISBN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pubname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_publishing'


class TbPurview(models.Model):
    id = models.IntegerField(primary_key=True)
    sysset = models.IntegerField(blank=True, null=True)
    readerset = models.IntegerField(blank=True, null=True)
    bookset = models.IntegerField(blank=True, null=True)
    borrowback = models.IntegerField(blank=True, null=True)
    sysquery = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_purview'


class TbReader(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=4, blank=True, null=True)
    barcode = models.CharField(max_length=30, blank=True, null=True)
    vocation = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    papertype = models.CharField(db_column='paperType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    paperno = models.CharField(db_column='paperNO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    createdate = models.DateField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(max_length=30, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    typeid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_reader'


class TbReadertype(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_readertype'
