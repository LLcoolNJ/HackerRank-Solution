import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args)throws Exception  {

		//BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Scanner inr = new Scanner (System.in);
		int t = inr.nextInt();
		BigInteger n[] = new BigInteger[t];
		BigInteger s[] = new BigInteger[t];
		BigInteger m = BigInteger.valueOf(100000);
		for(int i=0;i<t;i++){
			n[i] = inr.nextBigInteger();
		}
		for(int i=0;i<t;i++){
			s[i] = BigInteger.valueOf(2).modPow(n[i], m);
			s[i] = s[i].subtract(BigInteger.ONE);
			System.out.println(s[i]);
		}
	}

}
