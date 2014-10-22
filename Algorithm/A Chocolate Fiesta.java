import java.math.BigInteger;
import java.util.Scanner;


public class Solution {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int e = 0;
		int o = 0;
		int a[] = new int[n];
		for(int i=0;i<n;i++){
			int t = in.nextInt();
			a[i] = t;
			if(t%2==0){
				e++;
			}else{
				o++;
			}

		}
		BigInteger sum = BigInteger.ZERO;
		BigInteger s1  = BigInteger.ZERO;
		BigInteger s2 = BigInteger.ZERO;
		if(o==0){
			s2 = BigInteger.valueOf(2).pow(e);
			s2 = s2.subtract(BigInteger.ONE);
			sum = sum.add(s2);
		}else if(e==0){
			if(o>1){
			s1 = BigInteger.valueOf(2).pow(o-1);
			sum = sum.add(s1);
			sum = sum.subtract(BigInteger.ONE);
			}
		}
		else{
			s1 = BigInteger.valueOf(2).pow(o-1);
			s2 = BigInteger.valueOf(2).pow(e);		
			s2 = s2.subtract(BigInteger.ONE);
			sum = s1.multiply(s2);
			sum = sum.add(s1);
			sum = sum.subtract(BigInteger.ONE);
		}
		sum = sum.mod(BigInteger.valueOf(1000000007));
		System.out.println(sum);
	}
}
