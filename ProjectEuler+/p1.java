import java.util.*;

class Solution{
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int i=0;i<t;i++){
            long l = in.nextLong()-1;
            long s = 0;
            long n3 = l/3;
            long n5 = l/5;
            long n15 = l/15;
            s += 3*(n3*(n3+1))/2;
            s += 5*(n5*(n5+1))/2;
            s -= 15*(n15*(n15+1))/2;
            System.out.println(s);
        }
    }
    
}p1