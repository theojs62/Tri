# Tri insertion 

   Le tri par insertion consiste à prendre les éléments un par un, dans l'ordre de rangement dans la liste,
    et à les insérer dans une liste au bon emplacement. 

Tout d'abord, il faut importer le module *insertion.py* :

```
import insertion_sort
```

Pour ensuite utiliser le programme, il faut utiliser :

```
insertion_sort(N, accurate)

'''
## Explication du programme 

   Les nombres à trier est dans une liste.Il s'agit de trier cette liste  
   Le seul élément à mémoriser en plus est celui qui doit être inséré. On l'appelle la **N**. 
   La fonction de tri comporte une boucle d'indice n qui désigne l'élément à insérer. il faut décaler d'un rang vers la droite les éléments qui sont supérieurs à **N** ,en procédant par indice décroissant,à commencer par l'élément,
   Il faut donc écrire une boucle pour décaler ces éléments.On note j l'indice de cette boucle. 
   La boucle s'arrête lorsqu'on rencontre un nombre inférieur ou égal à N.
