import java.math.BigInteger;
import java.util.Scanner;


public class Solution {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in  = new Scanner(System.in);
		int t = in.nextInt();
		BigInteger n[] = new BigInteger[t];
		BigInteger s[] = new BigInteger[t];
		for (int i=0;i<t;i++){
			n[i] = in.nextBigInteger();
		}
		for(int i=0;i<t;i++){
			s[i] = n[i].modPow(BigInteger.valueOf(2), BigInteger.valueOf(1000000007));
		}
		for(BigInteger i: s){
			System.out.println(i);
		}

	}

}
