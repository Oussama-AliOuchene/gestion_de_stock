from django.urls import path
from . import views 



urlpatterns = [
   path('',views.home),
    # url produit
    path('create_product', views.create_product, name='create_product'),
    path('product_list' , views.product_list , name='product_list'),
    path('update_product/<str:code_produit>/', views.update_product, name='update_product'),
    path('delete_product/<str:code_produit>/', views.delete_product, name='delete_product'),

    # url fourniseur
    path('create_forniseur', views.create_forniseur  , name='create_forniseur'),
    path('fourniseur_list' , views.fourniseur_list , name='fourniseur_list'),
    path('update_fournisseur/<str:code_fournisseur>/', views.update_fournisseur, name='update_fournisseur'),
    path('delete_fournisseur/<str:code_fournisseur>/', views.delete_fournisseur, name='delete_fournisseur'),

    # url local
    path('create_local', views.create_local , name='create_local'),
    path('local_list' , views.local_list , name='local_list'),
    path('update_local/<str:code_local>/', views.update_local, name='update_local'),
    path('delete_local/<str:code_local>/', views.delete_local, name='delete_local'),
    
    # url bonsortie
    path('create_bonSortie', views.create_bonSortie, name="create_bonSortie"),
    path('bonSortie_list' , views.bonSortie_list , name='bonSortie_list'),
    path('updateBonSortie/<str:code_bon_sortie>/', views.updateBonSortie, name='updateBonSortie'),
    path('delete_bonSortie/<str:code_bon_sortie>/', views.delete_bonSortie, name='delete_bonSortie'),

    # url bonentrer
    path('create_BonEntrer', views.create_bonEntrer , name="create_BonEntrer"),
    path('bonEntrer_list' , views.bonEntrer_list , name='bonEntrer_list'),
    path('updateBonEntre/<str:code_bon_entre>/', views.updateBonEntrer, name='updateBonEntrer'),
    path('delete_bonEntrer/<str:code_bon_entre>/', views.delete_bonEntrer, name='delete_bonEntrer'),
    
    # url gestionaire
    path('create_gestionnaire', views.create_gestionnaire , name="create_gestionnaire"),
    path('gestionnaire_list' , views.gestionnaire_list , name='gestionnaire_list'),
    path('update_gestionnaire/<str:code_gestionnaire>/', views.update_gestionnaire, name='update_gestionnaire'),
    path('delete_gestionnaire/<str:code_gestionnaire>/', views.delete_gestionnaire, name='delete_gestionnaire'),
    # url sauvegarde de base de  donner 
    path('sauvegarder_base_de_donnees', views.sauvegarder_base_de_donnees, name='sauvegarder_base_de_donnees'),
]
