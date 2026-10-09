# 1. Définir la fonction F(n)
F_values = {
    1: 4, 2: 6, 3: 15, 4: 5,
    5: 3, 6: 2, 7: 4, 8: 5,
    9: 6, 10: 7, 11: 8, 12: 10,
    13: 9, 14: 8, 15: 7, 16: 3
}

def F(n):
    return F_values[n]


# 2. Fonction qui retourne les voisins de n
def voisins(n):
    if n == 1:
        return [2]
    elif n == 16:
        return [15]
    else:
        return [n - 1, n + 1]


# 3. Algorithme Hill Climbing simple (maximisation)
def hill_climbing(n_initial):
    courant = n_initial

    while True:
        print(f"n = {courant}, F(n) = {F(courant)}")

        # Obtenir valeur du nœud courant
        valeur_courante = F(courant)

        # Calculer les voisins
        v = voisins(courant)

        # Trouver le meilleur voisin
        meilleur_voisin = max(v, key=lambda x: F(x))
        valeur_meilleure = F(meilleur_voisin)

        # Si aucun voisin n'est meilleur → optimum local
        if valeur_meilleure <= valeur_courante:
            print("\nAucun voisin meilleur. Optimum local atteint.")
            break

        # Sinon on se déplace vers le meilleur voisin
        courant = meilleur_voisin


# 4. Exécuter avec n = 6
hill_climbing(1)
