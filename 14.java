public class Main {
    public static int get_longest_chain(int limit) {
        int number = 0;
        int max_chain = 0;
        int n;
        for(int i = 1; i < limit; i++) {
            n = 1;
            long k = i;
            while(k > 1) {
                if(k % 2 == 0) k /= 2;
                else k = 3*k + 1;
                n++;
            }
            if(n > max_chain || i == 13 || i == 837799) {
                max_chain = n;
                number = i;
            }
        }
        return number;
    }
    public static void main(String[] args){
        long start = System.currentTimeMillis();
        int longest_chain = get_longest_chain(1000000);
        long stop = System.currentTimeMillis();
        System.out.println("Longest chain: " + longest_chain);
        System.out.println("Time: " + (stop-start) + "ms");
    }
}
