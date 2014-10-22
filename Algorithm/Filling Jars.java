import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) throws Exception  {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s [] = br.readLine().split(" ");
		int n = Integer.parseInt(s[0]);
		int m = Integer.parseInt(s[1]);
		int a[] = new int[m];
		int b[] = new int[m];
		int k[] = new int[m];
		for(int i=0;i<m;i++){
			s = br.readLine().split(" ");
			a[i] = Integer.parseInt(s[0]);
			b[i] = Integer.parseInt(s[1]);
			k[i] = Integer.parseInt(s[2]);
		}
		BigInteger su = BigInteger.valueOf(0);
		for(int i=0;i<m;i++){
			//BigInteger su = BigInteger.valueOf(0);
			int l = b[i]-a[i]+1;
			su = su.add(BigInteger.valueOf(k[i]).multiply(BigInteger.valueOf(l)));
		}		
		su = su.divide(BigInteger.valueOf(n));
		System.out.println(su);

	}
}