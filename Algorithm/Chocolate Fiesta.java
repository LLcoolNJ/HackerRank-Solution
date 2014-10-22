import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args)  throws Exception  {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		int t = Integer.parseInt(s);
		String inp[] = new String [3];
		int [] n = new int[t];
		int [] c = new int[t];
		int [] m = new int[t];
		int [] oup = new int[t];
		for(int i=0;i<t;i++){
			s = br.readLine();
			inp = s.split(" ");
			n[i] = Integer.parseInt(inp[0]);
			c[i] = Integer.parseInt(inp[1]);
			m[i] = Integer.parseInt(inp[2]);
		}
		for(int i=0;i<t;i++){
			int su = n[i]/c[i];
			n[i] = n[i]/c[i];
			while (n[i]>=m[i]){
				su += n[i]/m[i];
				n[i] = n[i]/m[i] + n[i]%m[i];
			}
			oup[i] = su;
		}
		for(int i:oup){
			System.out.println(i);
		}
	}

}