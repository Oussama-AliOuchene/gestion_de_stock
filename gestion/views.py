from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
import os
import csv
from django.apps import apps
from .models import Produit , Fournisseur , Local , BonSortie ,  BonEntre ,Gestionnaire , ConfirmationEntre , ConfirmationSortie

# Create your views here.
def index(request) :
    return render(request , "index.html");

def home(request):

    number_produits = Produit.objects.count()
    number_fourniseur = Fournisseur.objects.count()
    number_local = Local.objects.count()
    number_gestionnaire = Gestionnaire.objects.count()
    number_BonEntre = BonEntre.objects.count()
    number_BonSortie = BonSortie.objects.count()
    return render(request , 'home.html' , {'number_BonSortie' : number_BonSortie , 'number_BonEntre' : number_BonEntre , 'number_produits' : number_produits , 'number_fourniseur' : number_fourniseur , 'number_local' : number_local , 'number_gestionnaire' :number_gestionnaire })

def create_product(request):
    fourniseur = Fournisseur.objects.all();
    if request.method == 'POST':
        code_produit = request.POST.get('code_produit')
        designation = request.POST.get('designation')
        date_fabrication = request.POST.get('date_fabrication')
        unite = request.POST.get('unite')
        quantite_stock = request.POST.get('quantite_stock')
        quantite_util = request.POST.get('quantite_util')
        quantite_vandale = request.POST.get('quantite_vandale')
        code_fournisseur_id =request.POST.get('code_fournisseur')
        fournisseur = Fournisseur.objects.get(code_fournisseur = code_fournisseur_id)        

        produit = Produit(
            code_produit=code_produit,
            designation=designation,
            date_fabrication=date_fabrication,
            unite=unite,
            quantite_stock=quantite_stock,
            quantite_util=quantite_util,
            quantite_vandale=quantite_vandale,
            code_fournisseur = fournisseur
        )
        

        produit.save()
        return redirect('product_list')

    return render(request, 'create_product.html' , {'fourniseurs' : fourniseur})


def product_list(request) :
    products = Produit.objects.all()
    return render(request , 'product_list.html' ,{'products' : products})



def update_product(request, code_produit):
    produit = get_object_or_404(Produit, code_produit=code_produit)
    fournisseur_list = Fournisseur.objects.all()

    # fourniseur = Fournisseur(produit.code_fournisseur.code_fournisseur)
    if request.method == 'POST':
        produit.designation = request.POST.get('designation')
        produit.date_fabrication = request.POST.get('date_fabrication')
        produit.unite = request.POST.get('unite')
        produit.quantite_stock = request.POST.get('quantite_stock')
        produit.quantite_util = request.POST.get('quantite_util')
        produit.quantite_vandale = request.POST.get('quantite_vandale')
        code_fournisseur_id = produit.code_fournisseur_id
        code_fournisseur = Fournisseur.objects.get(code_fournisseur = code_fournisseur_id).code_fournisseur
        produit.code_fournisseur_id = request.POST.get('code_fournisseur')
        
        
        produit.save()
        return redirect('product_list')
    
    return render(request, 'update_product.html', {'produit': produit , 'fourniseurs' :fournisseur_list })



def delete_product(request , code_produit):
    product = get_object_or_404(Produit , code_produit = code_produit)
    if request.method ==  'POST' : 
        product.delete()
        return redirect('product_list') 
    return render(request, 'delete_product.html', {'produit': product})

def recherche_produit(request) :
    
    resultats = Produit.objects.filter(designation = request.designation )



# ----------------------------------------------------------


def create_forniseur(request):
    if request.method == 'POST':
        code_fournisseur = request.POST.get('code_fournisseur')
        nom_fournisseur = request.POST.get('nom_fournisseur')
        prenom_fournisseur = request.POST.get('prenom_fournisseur')
        email = request.POST.get('email')
        numero_telephone = request.POST.get('numero_telephone')
        adresse = request.POST.get('adresse')
        pays = request.POST.get('pays')
        

        fournisseur = Fournisseur(
            code_fournisseur=code_fournisseur,
            nom_fournisseur=nom_fournisseur,
            prenom_fournisseur=prenom_fournisseur,
            email=email,
            numero_telephone=numero_telephone,
            adresse=adresse,
            pays=pays
        )


        fournisseur.save()
        return redirect ('fourniseur_list')
    return render(request, 'create_fournisseur.html')
def fourniseur_list(request) :
    fourniseur = Fournisseur.objects.all()
    return render(request , 'fournisseur_list.html' ,{'fournisseurs' : fourniseur})



def update_fournisseur(request, code_fournisseur):
    fournisseur = get_object_or_404(Fournisseur, code_fournisseur=code_fournisseur)
    
    if request.method == 'POST':
        fournisseur.code_fournisseur = request.POST.get('code_fournisseur')
        fournisseur.nom_fournisseur = request.POST.get('nom_fournisseur')
        fournisseur.prenom_fournisseur = request.POST.get('prenom_fournisseur')
        fournisseur.email = request.POST.get('email')
        fournisseur.numero_telephone = request.POST.get('numero_telephone')
        fournisseur.adresse = request.POST.get('adresse')
        fournisseur.pays = request.POST.get('pays')
        
        fournisseur.save()
        return redirect('fourniseur_list')
        
    
    return render(request, 'update_fournisseur.html', {'fournisseurs': fournisseur})



def delete_fournisseur(request , code_fournisseur):
    fournisseur = get_object_or_404(Fournisseur , code_fournisseur = code_fournisseur)
    if request.method ==  'POST' : 
        fournisseur.delete()
        return redirect('fourniseur_list')
        
    return render(request, 'delete_fournisseur.html', {'fournisseur': fournisseur})



def create_local(request):
    if request.method == 'POST':
        code_local = request.POST.get('code_local')
        adresse_local = request.POST.get('adresse_local')
       
        

        local = Local(
            code_local=code_local,
            adresse_local=adresse_local,
        )


        local.save()
        
        return redirect('local_list')
    return render(request, 'create_local.html')
def local_list(request) :
    local = Local.objects.all()
    return render(request , 'local_list.html' ,{'locals' : local})



def update_local(request, code_local):
    local = get_object_or_404(Local, code_local=code_local)
    
    if request.method == 'POST':
        local.code_local = request.POST.get('code_local')
        local.adresse_local = request.POST.get('adresse_local')
       
        local.save()
        return redirect('local_list')
    
    return render(request, 'update_local.html', {'local': local})



def delete_local(request , code_local):
    local = get_object_or_404(Local , code_local = code_local)
    if request.method ==  'POST' : 
        local.delete()
        return redirect('local_list') 
    return render(request, 'delete_local.html', {'local': local})



def create_bonSortie(request):
    # return HttpResponse(request.POST.get('code_produit') )
    produits = Produit.objects.all()
    if request.method == 'POST' :
        code_bon_sortie = request.POST.get('code_bon_sortie')
        date_sortie = request.POST.get('date_sortie')
        quantite_sortie = request.POST.get('quantite_sortie')
        
        code_produit_request = request.POST.get('code_produit') 
        code_produit = Produit.objects.get(code_produit = code_produit_request)
        
        if code_produit.quantite_stock < int(quantite_sortie) :
            return render( request ,'errour_de_qauntité_stock.html')

        code_produit.quantite_stock = code_produit.quantite_stock - int(quantite_sortie)
        
        code_produit.save()
        bon = BonSortie(
            code_bon_sortie = code_bon_sortie,
            date_sortie = date_sortie,
            quantite_sortie = quantite_sortie,
            code_produit = code_produit
        )
        bon.save()
        return redirect(bonSortie_list)
    return render(request, 'create_bonSortie.html' , {'produits' : produits})



def bonSortie_list(request) :
    bon = BonSortie.objects.all()
    return render(request , 'bonSortie_list.html' ,{'bons' : bon})



def updateBonSortie(request, code_bon_sortie):
    bon = get_object_or_404(BonSortie, code_bon_sortie=code_bon_sortie)
    produits = Produit.objects.all()
    if request.method == 'POST':
        bon.code_bon_sortie = request.POST.get('code_bon_sortie')
        bon.date_sortie = request.POST.get('date_sortie')
        bon.quantite_sortie = request.POST.get('quantite_sortie')
        code_produit = Produit(bon.code_produit_id).code_produit
        bon.code_produit_id = request.POST.get('code_produit')
        bon.save()
        return redirect(bonSortie_list)
    
    return render(request, 'undate_BonSorie.html', {'bon': bon , 'produits' : produits})



def delete_bonSortie(request , code_bon_sortie):
    bon = get_object_or_404(BonSortie , code_bon_sortie = code_bon_sortie)
    if request.method ==  'POST' : 
        bon.delete()
        return redirect('bonSortie_list') 
    return render(request, 'delete_bonSortie.html')
# BonEntrer



def create_bonEntrer(request):
    produits = Produit.objects.all()
    fournisseurs = Fournisseur.objects.all()
    if request.method == 'POST' :
        code_bon_entre = request.POST.get('code_bon_entre')
        date_entre = request.POST.get('date_entre')
        quantite_entre = request.POST.get('quantite_entre')
        
        code_produit_request = request.POST.get('code_produit') 
        code_produit = Produit.objects.get(code_produit = code_produit_request)
        
       
        code_produit.quantite_stock = code_produit.quantite_stock + int(quantite_entre)
        
        code_produit.save()
        bon = BonEntre(
            code_bon_entre = code_bon_entre,
            date_entre = date_entre,
            quantite_entre = quantite_entre,
            code_produit = code_produit
        )
        bon.save()

        code_fournisseur = request.POST.get('code_fournisseur')
        code_fournisseur_id = Fournisseur.objects.get(code_fournisseur = code_fournisseur)
        
        confirmation = ConfirmationEntre(
            code_bon_entre_id = code_bon_entre,
            code_fournisseur_id = code_fournisseur_id
        )
        confirmation.save()
        return redirect('bonEntrer_list')
    return render(request, 'create_bonEntrer.html' , {'produits' : produits , 'fournisseurs' : fournisseurs})



def bonEntrer_list(request) :
    bon = BonEntre.objects.all()
    return render(request , 'bonEntre_list.html' ,{'bons' : bon})

def updateBonEntrer(request, code_bon_entre):
    bon = get_object_or_404(BonEntre, code_bon_entre = code_bon_entre)
    produits = Produit.objects.all()
    if request.method == 'POST':
        bon.code_bon_entre = request.POST.get('code_bon_entre')
        bon.date_entre = request.POST.get('date_entre')
        bon.quantite_entre = request.POST.get('quantite_entre')
        code_produit = Produit(bon.code_produit_id).code_produit
        bon.code_produit_id = request.POST.get('code_produit')

        bon.save()
        return redirect(bonEntrer_list)
    
    return render(request, 'undate_BonEntrer.html', {'bon': bon , 'produits' : produits})




def delete_bonEntrer(request , code_bon_entre):
    bon = get_object_or_404(BonEntre , code_bon_entre = code_bon_entre)
    if request.method ==  'POST' : 
        bon.delete()
        return redirect(bonEntrer_list) 
    return render(request, 'delete_BonEntre.html', {'bon': bon})



# Gestionnaire


def create_gestionnaire(request):
    locals = Local.objects.all()
    if request.method == 'POST':
        code_gestionnaire = request.POST.get('code_gestionnaire')
        nom_gestionnaire = request.POST.get('nom_gestionnaire')
        prenom_gestionnaire = request.POST.get('prenom_gestionnaire')
        email = request.POST.get('email')
        numero_telephone = request.POST.get('numero_telephone')
        code_local_id = request.POST.get('code_local')


        gestionnaire = Gestionnaire(
            code_gestionnaire=code_gestionnaire,
            nom_gestionnaire=nom_gestionnaire,
            prenom_gestionnaire=prenom_gestionnaire,
            email=email,
            numero_telephone=numero_telephone,
            code_local_id=code_local_id,
        )
        gestionnaire.save()
        return redirect('gestionnaire_list')
        
    
    return render(request, 'create_gestionnaire.html' , {'locals' : locals})

def gestionnaire_list(request):
    gestionnaires = Gestionnaire.objects.all()
    return render(request, 'gestionnaire_list.html', {'gestionnaires': gestionnaires})

def update_gestionnaire(request, code_gestionnaire):
    gestionnaire = get_object_or_404(Gestionnaire, code_gestionnaire=code_gestionnaire)
    locals = Local.objects.all()
    if request.method == 'POST':
        gestionnaire.nom_gestionnaire = request.POST.get('nom_gestionnaire')
        gestionnaire.prenom_gestionnaire = request.POST.get('prenom_gestionnaire')
        gestionnaire.email = request.POST.get('email')
        gestionnaire.numero_telephone = request.POST.get('numero_telephone')
        gestionnaire.code_local_id = request.POST.get('code_local')
        gestionnaire.save()
        return redirect('gestionnaire_list')
    
    return render(request, 'update_gestionnaire.html', {'gestionnaire': gestionnaire , 'locals' : locals})

def delete_gestionnaire(request, code_gestionnaire):
    gestionnaire = get_object_or_404(Gestionnaire, code_gestionnaire=code_gestionnaire)
    if request.method == 'POST':
        gestionnaire.delete()
        return redirect('gestionnaire_list')
    
    return render(request, 'delete_gestionnaire.html', {'gestionnaire': gestionnaire})

# -------souvegarde la bd--------


def sauvegarder_base_de_donnees(request):
    dossier_principal_sauvegarde = '/Users/oussamaaliouchene/Desktop/sauvegarde_BD'
    
    nom_sous_dossier = request.GET.get('nom_sous_dossier', 'default_backup')
    
    dossier_sauvegarde = os.path.join(dossier_principal_sauvegarde, nom_sous_dossier)
    
    if not os.path.exists(dossier_sauvegarde):
        os.makedirs(dossier_sauvegarde)

    nom_app = 'gestion'

    for model in apps.get_app_config(nom_app).get_models():
        nom_table = model._meta.db_table
        chemin_fichier = os.path.join(dossier_sauvegarde, f'{nom_table}.csv')
        
        objets = model.objects.all()
        
        if objets.exists():
            with open(chemin_fichier, 'w', newline='') as fichier_csv:
                writer = csv.writer(fichier_csv)
                
                champs = [field.name for field in model._meta.fields]
                writer.writerow(champs)
                
                for obj in objets:
                    writer.writerow([getattr(obj, champ) for champ in champs])
    return render(request ,'save.html')
