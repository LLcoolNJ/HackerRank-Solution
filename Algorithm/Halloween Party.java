import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) throws Exception  {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		int t = Integer.parseInt(s);
		BigInteger inp[] = new BigInteger [t];
		int in[] = new int[t];
		for(int i=0;i<t;i++){
			in[i] = Integer.parseInt(br.readLine());
			inp[i] = BigInteger.valueOf(in[i]) ;
		}
		for(int i=0;i<t;i++){
			BigInteger su;
			BigInteger a = BigInteger.valueOf(in[i]).divide(BigInteger.valueOf(2));
			if(in[i]%2 == 0){
				//su = inp[i].multiply(inp[i]);
				//su = su.divide(BigInteger.valueOf(4));
				su = a.multiply(a);
			}else{
				//su = (inp[i]/2)*((inp[i]/2)+1);
				su = a.multiply(a);
				su = su.add(a);
			}
			System.out.println(su);
		}
	}

}