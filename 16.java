public class Main {
    private static int get_sum() {
        int digit_sum = 0;
        byte[] nums = new byte[350];
        nums[349] = 1;
        byte x;
        for(int i = 0; i < 1000; i++) {
            boolean shift = false;
            for (int j = 349; j >= 0; j--) {
                x = (byte)(nums[j] * 2);
                if(shift) x+=1;
                shift = false;
                if(x/10 == 1) shift = true;
                nums[j] = (byte)(x%10);
            }
        }
        for(int i = 0; i < 350; i++)
            digit_sum += nums[i];
        return digit_sum;
    }
    public static void main(String[] args){
        int sum = get_sum();
        System.out.println("\nDigit sum: " + sum);
    }
}
