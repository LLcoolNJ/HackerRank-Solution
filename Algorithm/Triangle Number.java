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
		int n[] = new int[t];
		for(int i=0;i<t;i++){
			n[i] = inr.nextInt();
		}
		for(int i:n){
			if(i%2 != 0){
				System.out.println('2');
			}else{
				int k = i/2;
				if(k%2 == 0){
					System.out.println('3');
				}else{
					System.out.println('4');
				}
			}
		}
	}

}
