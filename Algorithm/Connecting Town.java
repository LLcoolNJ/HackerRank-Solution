import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) throws Exception  {

		//BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Scanner inr = new Scanner (System.in);
		int t = inr.nextInt();
		int n[] = new int [t];
		BigInteger  a[][] = new BigInteger [t][100];
		BigInteger s[] = new BigInteger[t];
		for(int i=0;i<t;i++){
			s[i] = BigInteger.ONE;
			n[i] = inr.nextInt();
			for(int j=0;j<n[i]-1;j++){
				a[i][j] = inr.nextBigInteger();
			}
		}
		for(int i=0;i<t;i++){
			for(int j=0;j<n[i]-1;j++){
				s[i] = s[i].multiply(a[i][j]);
			}
			s[i] = s[i].mod(BigInteger.valueOf(1234567));
		}
		for(BigInteger i: s){
			System.out.println(i);
		}
	}

}
