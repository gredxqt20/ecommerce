Fichier README du projet Ecommerce
Ce projet est une boutique en ligne construite à l'aide de Django et MySQL. Il permet aux utilisateurs de parcourir des produits, d'ajouter des articles à leur panier et d'acheter des articles. Il comprend également un panneau d'administration où les administrateurs peuvent gérer les produits, les catégories et les commandes.

Dépendances
Les dépendances suivantes sont nécessaires pour exécuter ce projet :

Django
MySQL
Pillow
Jazzmin

Installation
Clonez ce référentiel sur votre machine locale.
Installez les dépendances requises jazzmine ,django,python,pillow,mysql .
Créez une nouvelle base de données 'ecommerce' MySQL pour le projet.
Configurez les paramètres de la base de données dans le fichier settings.py, sous le dictionnaire DATABASES.
Exécutez les commandes suivantes dans votre terminal pour configurer la base de données et créer un superutilisateur :
Copy code
python manage.py migrate
python manage.py createsuperuser
Lancez le serveur de développement en utilisant la commande python manage.py runserver.

Authentification
L'authentification est requise pour accéder à certaines fonctionnalités du site, comme passer une commande ou accéder au panneau d'administration. Les utilisateurs peuvent créer un compte en cliquant sur le bouton "S'inscrire" dans la barre de navigation, ou se connecter en utilisant leur adresse e-mail et leur mot de passe.

Ajout de produits et de catégories
Pour ajouter de nouveaux produits ou catégories, connectez-vous au panneau d'administration en utilisant vos identifiants de superutilisateur. Accédez à la section "Produits" ou "Catégories" et cliquez sur le bouton "Ajouter" pour créer un nouvel élément.

Utilisation
Ajout de produits et de catégories
Pour ajouter de nouveaux produits ou catégories, connectez-vous au panneau d'administration en utilisant vos identifiants de superutilisateur. Accédez à la section "Produits" ou "Catégories" et cliquez sur le bouton "Ajouter" pour créer un nouvel élément.

Acheter des produits
Les utilisateurs peuvent acheter des produits en ajoutant des articles à leur panier et passer leur commandes. Pour ajouter des articles au panier, cliquez sur le bouton "Ajouter au panier" sur la page du produit. Pour passer votre commande, cliquez sur le bouton "Checkout", vérifiez votre commande et cliquez sur "Commander" pour finaliser votre achat.

Consulter les commandes établies et l'historique
Les utilisateurs peuvent consulter l'ensemble des commandes passées en cliquant sur "My orders" et avoir des leurs details de la livraison et les details du produit en cliquant dur "View" présentant devant chaque commande. 
