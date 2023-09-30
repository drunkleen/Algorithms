/*
*   In mathematics, the Fibonacci sequence is a sequence in which each
*   number is the sum of the two preceding ones. The Fibonacci numbers
*   may be defined by the recurrence relation.

*   F(n) = F(n-1) + F(n-2)
*   where F(0) = F(1) = 1
*/

import java.util.HashMap;

public class fibonacciAlgorithm{
    public static void  main(String[] args) {
        long num = 21;
        System.out.println("the "+ num + "th fibonacci num is:" + fib(num));
    }

    public static long fib(long n) {
        return fib(n, new HashMap<Long, Long>());
    }

    public static long fib(long n, HashMap<Long, Long> mapDict) {
        if (n == 0 || n == 1) {return n;}
        if (mapDict.containsKey(n)) {
            return mapDict.get(n);
        }

        long result = fib(n - 1, mapDict) + fib(n - 2, mapDict);
        mapDict.put(n, result);
        return result;
    }
}


