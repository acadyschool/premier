#include <stdio.h>
#include <stdlib.h>

int main() {
    int *tableau;
    int taille;

    // Demande de la taille du tableau
    printf("Entrez la taille du tableau : ");
    scanf("%d", &taille);

    // Allocation dynamique de mémoire
    tableau = (int *)malloc(taille * sizeof(int));

    // Vérification de l'allocation
    if (tableau == NULL) {
        printf("Erreur d'allocation mémoire !\n");
        return 1;
    }

    // Remplissage du tableau
    for (int i = 0; i < taille; i++) {
        tableau[i] = i * 2;  // Remplissage avec des valeurs (exemple : multiples de 2)
    }

    // Affichage des valeurs
    printf("Contenu du tableau :\n");
    for (int i = 0; i < taille; i++) {
        printf("%d ", tableau[i]);
    }
    printf("\n");

    // Libération de la mémoire allouée
    free(tableau);
    printf("Mémoire libérée avec succès.\n");

    return 0;
}

