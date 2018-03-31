public class Main {
    public static boolean isPrime(int n) {
        if(n == 2)
            return true;
        for(int i = 2; i < Math.sqrt(n)+1; i++)
            if(n % i == 0)
                return false;
        return true;
    }
    public static void main(String[] args) {
        long sum = 0;
        for(int i = 2; i < 2000000; i++)
            if(isPrime(i))
                sum += i;
        System.out.println(sum);
    }
}
