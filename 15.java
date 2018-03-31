public class Main {
    public static long get_routes_count(int n) {
        Double count = 1.0;
        for(int i = 1; i <= n; i++) {
            count *= (double)(n + i) / i;
        }
        return (long)Math.round(count);
    }
    public static void main(String[] args){
        long routes = get_routes_count(20);
        System.out.println("Routes: " + routes);
    }
}
