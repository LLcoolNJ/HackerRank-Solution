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
		int ki[] = new int [n];
		int k = inr.nextInt();
		for(int i=0;i<n;i++){
			ki[i] = inr.nextInt();
		}
		Arrays.sort(ki);
		int min = ki[k-1] - ki[0];
		for(int i=0;i<n-k-1;i++){
			if(ki[k+i]-ki[i+1]<min){
				//System.out.println(min);
				min  = ki[k+i] - ki[i+1];
			}
		}
		
		System.out.println(min);
	}

}
