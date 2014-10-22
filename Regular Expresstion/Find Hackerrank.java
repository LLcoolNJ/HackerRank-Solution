import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) throws Exception{
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        String h = "hackerrank";
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String inp = br.readLine();
		int n = Integer.parseInt(inp);
		for(int i=0;i<n;i++){
			inp = br.readLine();
			inp.toLowerCase();
			if (inp.startsWith(h) && inp.endsWith(h)){
				System.out.println(0);
			}else if(inp.startsWith(h)){
				System.out.println(1);
			}else if(inp.endsWith(h)){
				System.out.println(2);
			}else{
				System.out.println(-1);
			}
        }
    }
}