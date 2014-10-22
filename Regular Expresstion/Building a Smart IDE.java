import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void main(String[] args) throws Exception  {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String [] line = new String[200];
		int i = 0;
		line[i] = br.readLine();
		while(line[i] != null){
			i++;
			line[i] = br.readLine();
			
		}
		getComment(line);
	}

	private static void getComment(final String[] line) {
		// TODO Auto-generated method stub
		for (int i = 0;line[i] != null; i++){
			if(line[i].indexOf("/*")>=0){
				int l = line[i].indexOf("/*");
				if (line[i].indexOf("*/")>=0){
					int la = line[i].indexOf("*/");
					System.out.println(line[i].substring(l, la+2));
				}else{
					System.out.println(line[i].substring(l));
					i++;
					while(line[i].indexOf("*/")<0){
						System.out.println(line[i]);
						i++;
					}
					int la = line[i].indexOf("*/");
					System.out.println(line[i].substring(0, la+2));
				}
			}else if(line[i].indexOf("//")>=0){
				int l = line[i].indexOf("//");
				System.out.println(line[i].substring(l));
			}
		}
	}
}
