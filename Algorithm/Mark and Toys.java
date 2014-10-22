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
		int k = inr.nextInt();
		int toy[] = new int [n];
		for(int i=0;i<n;i++){
			toy[i] = inr.nextInt();
		}
		Arrays.sort(toy);
		int tot = 0;
		int total = 0;
		for(int i=0;i<n;i++){
			tot += toy[i];
			if(tot>k){
				break;
			}
			total++;
		}
		System.out.println(total);
	}

}
