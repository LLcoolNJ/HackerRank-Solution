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
		int ar[] = new int[n];
		for(int i=0;i<n;i++){
			ar[i] = inr.nextInt();
		}
		Arrays.sort(ar);
		int min = 10000000;//ar[1] - ar[0];
		int minar[] = new int[n];
		int j=0;
		minar[j] = 0;
		j++;
		for(int k=0;k<n-1;k++){
			if((ar[k+1]-ar[k])<min){
				j = 0;
				min = ar[k+1]-ar[k];
				minar[j] = k;
				j++;
			}else if((ar[k+1]-ar[k])==min){
				minar[j] = k;
				j++;
			}
			//System.out.println(j);
			//for(int l: ar){
			//	System.out.print(l + " ");
			//}
		}
		for(int i=0;i<j;i++){
			System.out.print(ar[minar[i]]+" "+ar[minar[i]+1]);
			System.out.print(" ");
		}
	}

}
