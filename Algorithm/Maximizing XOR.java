import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
/*
 * Complete the function below.
 */
public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		BigInteger l = in.nextBigInteger();
		BigInteger r = in.nextBigInteger();
		int i = l.intValue();
		int last = r.intValue();
		int j = last;
		BigInteger max = BigInteger.valueOf(i).xor(BigInteger.valueOf(j));
		for(i=l.intValue();i<last;i++){
			for(j=last;j>i;j--){
				if(max.compareTo(BigInteger.valueOf(i).xor(BigInteger.valueOf(j))) ==-1){
					max = BigInteger.valueOf(i).xor(BigInteger.valueOf(j));
				}
			}
			
		}
		System.out.println(max);
	}
}
