package edu;

public class principal {

    public static void main(String[] args) {
        Fatorial fatorial = new Fatorial();

        int fatorialRecursivo = fatorial.fatorialRecursivo(5);
        System.out.println("Fatorial com Recursividade");
        System.out.println(fatorialRecursivo);

        System.out.println("Fatorial sem Recursividade");
        int fatorialNaoRecursivo = fatorial.fatorialNaoRecursivo(5);
        System.out.println(fatorialNaoRecursivo);

        Fibonacci fibonacci = new Fibonacci();
        System.out.println("Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...");
        System.out.println("Posicoes : 0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10, 11,  12,  13, ...");
        
        int p1 = 7;
        System.out.println("\nFibonacci com Recursividade - posicao "+p1);
        int fibonacciRecursivo = fibonacci.fibonacciRecursivo(p1);
        System.out.println("valor = " + fibonacciRecursivo);

        int p2 = 11;
        System.out.println("Fibonacci sem Recursividade - posicao "+p2);
        int fibonacciNaoRecursivo = fibonacci.fibonacciNaoRecursivo(p2);
        System.out.println("valor = " + fibonacciNaoRecursivo);
    }
}
