# -*- coding: utf-8 -*-

from django.db import models

RADOP_CHECK_TYPES = (
    ('=', '='),
    (':=', ':='),
    ('==', '=='),
    ('+=', '+='),
    ('!=', '!='),
    ('>', '>'),
    ('>=', '>='),
    ('<', '<'),
    ('<=', '<='),
    ('=~', '=~'),
    ('!~', '!~'),
    ('=*', '=*'),
    ('!*', '!*'),
)

RADOP_REPLY_TYPES = (
    ('=', '='),
    (':=', ':='),
    ('+=', '+='),
)

NAS_TYPES = (
    ('cisco', 'cisco'),
    ('computone', 'computone'),
    ('livingston', 'livingston'),
    ('max40xx', 'max40xx'),
    ('mikrotik', 'mikrotik'),
    ('multitech', 'multitech'),
    ('netserver', 'netserver'),
    ('pathras', 'pathras'),
    ('patton', 'patton'),
    ('portslave', 'portslave'),
    ('tc', 'tc'),
    ('usrhiper', 'usrhiper'),
    ('other', 'other'),
)


class Cui(models.Model):
    clientipaddress = models.CharField(max_length=15)
    callingstationid = models.CharField(max_length=50)
    username = models.CharField(max_length=64)
    cui = models.CharField(max_length=32)
    creationdate = models.DateTimeField()
    lastaccounting = models.DateTimeField()

    def __str__(self):
        return str(self.clientipaddress)

    class Meta:
        db_table = 'cui'
        verbose_name_plural = "Cui"


class Nas(models.Model):
    nasname = models.CharField(max_length=128, unique=True)
    shortname = models.CharField(max_length=32)
    type = models.CharField(max_length=30, choices=NAS_TYPES)
    ports = models.IntegerField(blank=True, null=True)
    secret = models.CharField(max_length=60)
    server = models.CharField(max_length=64, blank=True, null=True)   
    community = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.nasname)

    class Meta:
        db_table = 'nas'
        verbose_name_plural = "nas"


class Radpostauth(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(db_column='pass', max_length=64)
    reply = models.CharField(max_length=32)
    authdate = models.DateTimeField()

    def __str__(self):
        return str(self.username)

    class Meta:
        db_table = 'radpostauth'
        verbose_name_plural = "radpostauth"


class Radreply(models.Model):
    username = models.CharField(max_length=30)
    attribute = models.CharField(max_length=30)
    op = models.CharField(max_length=2, choices=RADOP_REPLY_TYPES)
    value = models.CharField(max_length=40)

    def __str__(self):
        return str(self.username)

    class Meta:
        db_table = 'radreply'
        verbose_name_plural = "radreply"


class Radusergroup(models.Model):
    username = models.CharField(max_length=30)
    groupname = models.CharField(max_length=30)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return str(self.username)

    class Meta:
        db_table = 'radusergroup'


class Radcheck(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2, choices=RADOP_CHECK_TYPES)
    value = models.CharField(max_length=253)

    def __str__(self):
        return str(self.username)

    class Meta:
        db_table = 'radcheck'
        verbose_name_plural = "radcheck"


class Radgroupcheck(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2, choices=RADOP_CHECK_TYPES)
    value = models.CharField(max_length=253)

    class Meta:
        db_table = 'radgroupcheck'
        verbose_name_plural = "radgroupcheck"


class Radgroupreply(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2, choices=RADOP_REPLY_TYPES)
    value = models.CharField(max_length=253)

    def __str__(self):
        return str(self.groupname)

    class Meta:
        db_table = 'radgroupreply'
        verbose_name_plural = "radgroupreply"


class Radippool(models.Model):
    pool_name = models.CharField(max_length=64, help_text='The IP Pool name')
    framedipaddress = models.CharField(max_length=15)
    nasipaddress = models.CharField(max_length=16, blank=True, null=True)
    calledstationid = models.CharField(max_length=30, blank=True, null=True)
    callingstationid = models.CharField(max_length=30, blank=True, null=True)
    expiry_time = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    groupname = models.CharField(max_length=30, blank=True, null=True)
    pool_key = models.CharField(max_length=30, default=0)

    def __str__(self):
        return str(self.framedipaddress)

    class Meta:
        db_table = 'radippool'
        verbose_name_plural = "radippool"


class Radacct(models.Model):
    radacctid = models.AutoField(primary_key=True)
    acctsessionid = models.CharField(max_length=32)
    acctuniqueid = models.CharField(max_length=32)
    username = models.CharField(max_length=253, null=True)
    realm = models.CharField(max_length=64, null=True)
    nasipaddress = models.IPAddressField()
    nasportid = models.CharField(max_length=15, null=True)
    nasporttype = models.CharField(max_length=32, null=True)
    acctstarttime = models.DateTimeField(null=True)
    acctstoptime = models.DateTimeField(null=True)
    acctsessiontime = models.BigIntegerField(null=True)
    acctauthentic = models.CharField(max_length=32, null=True)
    acctinputoctets = models.BigIntegerField(null=True)
    acctoutputoctets = models.BigIntegerField(null=True)
    calledstationid = models.CharField(max_length=50, null=True)
    callingstationid = models.CharField(max_length=50, null=True)
    framedipaddress = models.IPAddressField(null=True)
    connectinfo_start = models.CharField(max_length=50, null=True)
    connectinfo_stop = models.CharField(max_length=50, null=True)
    acctterminatecause = models.CharField(max_length=32, null=True)
    servicetype = models.CharField(max_length=32, null=True)
    framedprotocol = models.CharField(max_length=32, null=True)
    acctstartdelay = models.IntegerField(null=True)
    acctstopdelay = models.IntegerField(null=True)
    xascendsessionsvrkey = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.acctuniqueid)

    class Meta:
        db_table = 'radacct'
        verbose_name_plural = "radacct"
