taches = []

while True:
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche   2. Afficher   0. Quitter")
    taches = []

while True:
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche   2. Afficher   3. Rechercher   0. Quitter")
    choix = input("Votre choix : ").strip()

    if choix == "1":
        titre = input("Titre de la tâche : ").strip()
        if titre == "":
            print("Erreur : le titre ne peut pas être vide.")
        else:
            taches.append(titre)
            print("Tâche ajoutée avec succès.")

    elif choix == "2":
        if len(taches) == 0:
            print("La liste des tâches est vide.")
        else:
            print("\nListe des tâches :")
            for i in range(len(taches)):
                print(f"{i + 1}. {taches[i]}")

    elif choix == "3":
        mot_cle = input("Mot-clé à rechercher : ").strip().lower()
        trouve = False
        print("\nRésultats de la recherche :")
        for i in range(len(taches)):
            if mot_cle in taches[i].lower():
                print(f"{i + 1}. {taches[i]}")
                trouve = True
        if not trouve:
            print("Aucune tâche ne correspond à ce mot-clé.")

    elif choix == "0":
        print("Au revoir !")
        break

    else:
        print("Erreur : option invalide.")