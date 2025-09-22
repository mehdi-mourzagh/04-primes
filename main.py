"""Affiche les nombres premiers de 0 à 99."""
from math import sqrt

def is_prime(p):
    """Retourne True si p est un nombre premier, False sinon."""
    if p < 2:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

def main():
    """Affiche les nombres premiers de 0 à 99 sur une ligne."""
    for n in range(100):
        if is_prime(n):
            print(n, end=" ")
    print()

if __name__ == "__main__":
    main()
