# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BaseAdmintable(models.Model):
    id = models.BigAutoField(primary_key=True)
    statut = models.IntegerField()
    user_id = models.IntegerField(unique=True)
    field_user_name_field = models.CharField(db_column="'user_name'", max_length=255)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_age_field = models.CharField(db_column="'age'", max_length=255)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_name_field = models.CharField(db_column="'name'", max_length=255)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_client_field = models.CharField(db_column="'client'", max_length=255)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    find = models.CharField(max_length=255)
    me = models.CharField(max_length=255)
    fournisseur = models.CharField(max_length=255)
    datep = models.CharField(max_length=255)
    datepp = models.CharField(max_length=255)
    datpp = models.CharField(max_length=255)
    atpp = models.CharField(max_length=255)
    tpp = models.CharField(max_length=255)
    tprp = models.CharField(max_length=255)
    tprpd = models.CharField(max_length=255)
    tprrpd = models.CharField(max_length=255)
    tprerpd = models.CharField(max_length=255)
    tpd = models.CharField(max_length=255)
    tpf = models.CharField(max_length=255)
    tpr = models.CharField(max_length=255)
    tprt = models.CharField(max_length=255)
    tprttt = models.CharField(max_length=255)
    thiings = models.CharField(max_length=255)
    thiingso = models.CharField(max_length=255)
    thiingo = models.CharField(max_length=255)
    thiino = models.CharField(max_length=255)
    thiinpo = models.CharField(max_length=255)
    codefournisseursage = models.CharField(max_length=255)
    codefournisseur = models.CharField(max_length=255)
    code_fournisseur = models.CharField(max_length=255)
    code_commande = models.CharField(max_length=255)
    paiment = models.CharField(max_length=255)
    paiment_devise = models.CharField(max_length=255)
    paiment_avance = models.CharField(max_length=255)
    date_arrivee = models.CharField(max_length=255)
    date_sortie = models.CharField(max_length=255)
    date_livraison = models.CharField(max_length=255)
    ccap = models.CharField(max_length=255)
    cap = models.CharField(max_length=255)
    date_cacrs = models.CharField(max_length=255)
    date_cars = models.CharField(max_length=255)
    hamdi = models.CharField(max_length=255)
    hamza = models.CharField(max_length=255)
    mohamed = models.CharField(max_length=255)
    omar = models.CharField(max_length=255)
    buraeu = models.CharField(max_length=255)
    casa = models.CharField(max_length=255)
    google = models.CharField(max_length=255)
    interlux = models.CharField(max_length=255)
    inter = models.CharField(max_length=255)
    testmohamed = models.CharField(max_length=255)
    testhamza = models.CharField(max_length=255)
    testouhemmi = models.CharField(max_length=255)
    typearticle = models.DateField(blank=True, null=True)
    date_sortie_depo = models.DateField(db_column='date sortie depo', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    type_transport = models.CharField(db_column='type transport', max_length=255)  # Field renamed to remove unsuitable characters.
    dedounement = models.CharField(max_length=255)
    zoneindustriele = models.CharField(max_length=255)
    quantitedisponible = models.BigIntegerField()
    quantitestock = models.BigIntegerField()
    test = models.DateField(blank=True, null=True)
    testtwo = models.DateField(blank=True, null=True)
    testtree = models.BigIntegerField()
    testfour = models.BigIntegerField()
    four = models.BigIntegerField()
    five = models.BigIntegerField()
    six = models.BigIntegerField()
    fin = models.CharField(max_length=255)
    portnumber = models.BigIntegerField()
    numerochasse = models.BigIntegerField()
    localisation = models.DateField(blank=True, null=True)
    etape = models.CharField(max_length=200)
    medd = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'base_admintable'
