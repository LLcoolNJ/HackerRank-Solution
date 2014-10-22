import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) throws Exception  {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		int n = Integer.parseInt(s);
		String [] ip = new String[n];
		for(int i = 0;i<n;i++){
			ip[i] = br.readLine();
		}
		for (int i= 0 ; i<n; i++){
			validate(ip[i]);
		}
	}
	public static void validate(final String ip){
		Pattern pat;
		Matcher match;
		String ip4 = "IPv4";
		String ip6 = "IPv6";
		String non = "Neither";
		final String ipv4 = 
				"^([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." +
				"([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." +
				"([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." +
				"([01]?\\d\\d?|2[0-4]\\d|25[0-5])$";
		final String ipv6 = 
				"^[0-9a-f]{1,4}:" + "[0-9a-f]{1,4}:" +
				"[0-9a-f]{1,4}:" + "[0-9a-f]{1,4}:" +
				"[0-9a-f]{1,4}:" + "[0-9a-f]{1,4}:" +
				"[0-9a-f]{1,4}:" + "[0-9a-f]{1,4}$";
		
		if(ip.indexOf(".")>0){
			pat = Pattern.compile(ipv4);
			match = pat.matcher(ip);
			if(match.matches()){
				System.out.println(ip4);
			}else{
				System.out.println(non);
			}
		}else if (ip.indexOf(":")>0){
			pat = Pattern.compile(ipv6);
			match = pat.matcher(ip);
			if(match.matches()){
				System.out.println(ip6);
			}else{
				System.out.println(non);
			}
		}else{
			System.out.println(non);
		}
	}

}
