import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) throws Exception  {

		//BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Scanner inr = new Scanner (System.in);
		int n = inr.nextInt();
		BigDecimal s = BigDecimal.valueOf(0.0) ;
		int b[] = new int[n];
		for(int i=0;i<n;i++){
			b[i] = inr.nextInt();
		}
		for (int i:b){
			BigDecimal p = BigDecimal.valueOf(i).divide(BigDecimal.valueOf(2.0));
			s = s.add(p);
		}
		System.out.println(s);
	}

}
