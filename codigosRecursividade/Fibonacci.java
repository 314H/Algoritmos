package edu;

public class Fibonacci {

    // Serie de números, tais que, definindo seus dois primeiros
    // numeros como sendo 0 e 1, os numeros seguintes sao obtidos
    // atraves da soma dos seus dois antecessores.
    // 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377...

    public int fibonacciRecursivo(int x) {
        if (x <= 1) {
            return x;
        } else {
            int v1 = fibonacciRecursivo(x - 1);
            int v2 = fibonacciRecursivo(x - 2);
            int valor = v1+v2;
            return  valor;
        }
    }

    public int fibonacciNaoRecursivo(int x) {
        int x0 = 0;
        int x1 = 1;
        int x2;
        for (int i = 0; i < x ; i++) {
            x2 = x0 + x1;
            x0 = x1;
            x1 = x2;
        }
        return x0;
    }
}
