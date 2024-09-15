from django.db import models

# Create your models here.

class Fournisseur(models.Model):
    code_fournisseur = models.CharField(max_length=100, primary_key=True)
    nom_fournisseur = models.CharField(max_length=50)
    prenom_fournisseur = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    numero_telephone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    adresse = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom_fournisseur} {self.prenom_fournisseur}"

class Local(models.Model):
    code_local = models.CharField(max_length=100, primary_key=True)
    adresse_local = models.CharField(max_length=100)

    def __str__(self):
        return self.adresse_local

class Produit(models.Model):
    code_produit = models.CharField(max_length=100, primary_key=True)
    designation = models.CharField(max_length=100)
    date_fabrication = models.DateField(null=True, blank=True )
    unite = models.CharField(max_length=50, null=True, blank=True)
    quantite_stock = models.IntegerField()
    quantite_util = models.IntegerField()
    quantite_vandale = models.IntegerField()
    code_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.SET_NULL, null=True, blank=True)

class BonEntre(models.Model):
    code_bon_entre = models.CharField(max_length=100, primary_key=True)
    date_entre = models.DateField(null=True, blank=True)
    quantite_entre = models.IntegerField()
    code_produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.code_bon_entre

class BonSortie(models.Model):
    code_bon_sortie = models.CharField(max_length=100, primary_key=True)
    date_sortie = models.DateField(null=True, blank=True)
    quantite_sortie = models.IntegerField()
    code_produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.code_bon_sortie

class ConfirmationEntre(models.Model):
    code_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    code_bon_entre = models.ForeignKey(BonEntre, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('code_fournisseur', 'code_bon_entre'),)

class ConfirmationSortie(models.Model):
    code_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    code_bon_sortie = models.ForeignKey(BonSortie, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('code_fournisseur', 'code_bon_sortie'),)

class Gestionnaire(models.Model):
    code_gestionnaire = models.CharField(max_length=100, primary_key=True)
    nom_gestionnaire = models.CharField(max_length=50)
    prenom_gestionnaire = models.CharField(max_length=50)
    email = models.EmailField()
    numero_telephone = models.CharField(max_length=15)
    code_local = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nom_gestionnaire} {self.prenom_gestionnaire}"

class Inventaire(models.Model):
    code_inventaire = models.CharField(max_length=100, primary_key=True)
    date_inventaire = models.DateField(null=True, blank=True)
    res = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.code_inventaire

    def __str__(self):
        return self.designation

class ProduitLocal(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('produit', 'local'),)
