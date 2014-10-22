import java.math.BigInteger;
import java.util.Scanner;


public class Solution {

	static BigInteger tw = BigInteger.ONE;
	static BigInteger tl = BigInteger.ONE;
	static BigInteger num = BigInteger.ONE;
	static BigInteger den = BigInteger.ONE;
	static BigInteger v24 = BigInteger.ONE;
	
	public static void main(String[] args) {
 
		Scanner in = new Scanner(System.in);
		int a = in.nextInt();
		int b = in.nextInt();
		BigInteger mo = BigInteger.valueOf(1000000007);
		BigInteger way = BigInteger.ZERO;
		if(a ==25 && b==24){
		}else if(a<25 && b<25){
		}else if((a == 25 && b<24) || (b == 25 && a<24)){
			
			int c;
			if(a == 25){
				tw = BigInteger.valueOf(a-1+b);
				tl = BigInteger.valueOf(b);
				c = b;
			}else{
				tw = BigInteger.valueOf(b-1+a);
				tl = BigInteger.valueOf(a);
				c = a;
			}
			
			for(int i=1;i<=c;i++){
				num = num.multiply(tw);
				tw = tw.subtract(BigInteger.ONE);
				den = den.multiply(tl);
				tl = tl.subtract(BigInteger.ONE);
			}
			way = num.divide(den).mod(mo);
			
			
		}else if((a-b==2) || (b-a==2)){
			
			v24 = BigInteger.valueOf(801728689);
			num = v24;
			int c;
			if(a>b){
				c = b - 24;
			}else{
				c = a - 24;
			}
			tw = BigInteger.valueOf(2);
			tw = tw.modPow(BigInteger.valueOf(c+1), mo);
			way = num.multiply(tw).mod(mo);
			
		}
		
		System.out.println(way);
	}

}
//32247603683100
