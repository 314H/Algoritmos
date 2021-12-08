package edu;

public class Fatorial {
    
    public int fatorialRecursivo(int x) {
        if (x == 0)
            return 1;
        
        int valor = x * fatorialRecursivo(x-1);
        return valor;
    }

    public int fatorialNaoRecursivo(int x) {
        int y = 1;
        while (x > 1) {
            y *= x; // y = y * x 
            x -= 1; // decrecimo de 1
        }
        return y;
    }
}


