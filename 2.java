public class Main {
    public static void main(String[] args) {
        int x = 1;
        int y = 1;
        int sum = 0;
        int tmp;
        while(y <= 4000000) {
            tmp = y;
            y = x + y;
            x = tmp;
            if(y%2 == 0)
                sum += y;
        }
        System.out.println(sum);
    }
}
