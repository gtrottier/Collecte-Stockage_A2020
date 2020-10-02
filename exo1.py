#Gabriel Trottier

"""[1-2] Fonction (avec arguments)
a) Écrire une fonction qui retourne le carré de son argument (x*x)
b) Écrire trois fonctions qui calculent respectivement le produit, la somme et la
division de deux arguments qui sont pris chacun au carré (question 1.a)
"""
#a
def square(x):
    return x*x
#b
def product1(x,y):
    return square(x)*square(y)
def sum1(x,y):
    return square(x)+square(y)
def div1(x,y):
    return square(x)/square(y)

"""
[3-4] Fonction (avec arguments)
a) Écrire une fonction qui retourne le cube de son argument (x*x*x)
b) Écrire trois fonctions qui calculent respectivement le produit, la somme et la
division de deux arguments qui sont pris chacun au cube (question 1.a)
[5] Écrire une fonction récursive qui permet de faire les calculs suivants :
 10+8+6+4+2+0
 20+18+16+14+12+10+8+6+4+2+0
 7+5+3+1
"""
#3-4
def cube(x):
    return x*x*x
def prod2(x,y):
    return cube(x)*cube(y)
def sum2(x,y):
    return cube(x)+cube(y)
def div2(x,y):
    return cube(x)/cube(y)
#5
def recu(n):
    if(n-2 < 2):
        return n
    else:
        return n + recu(n-2)
#[6] Écrire un programme qui multiplie deux listes
def list_prod(listA, listB):
    n = min(len(listA), len(listB))
    listC = [listA[i]*listB[i] for i in range(0,n)]
    return listC

"""
[7] Écrire un programme qui Affiche la table de multiplication par 8 en une seule
commande avec les instructions range() et list()
"""
#7
print([x*8 for x in range(1,15)])
