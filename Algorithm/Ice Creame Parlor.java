import java.util.Scanner;


public class Solution {

	/**
	 * @param args
	 */
	public static void main(String[] args)throws Exception  {

		//BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Scanner inr = new Scanner (System.in);
		int t = inr.nextInt();
		int m[] = new int[t];
		int n[] = new int[t];
		int c[][] = new int[t][10000];
		for(int i=0;i<t;i++){
			m[i] = inr.nextInt();
			n[i] = inr.nextInt();
			for(int j=0;j<n[i];j++){
				c[i][j] = inr.nextInt();
			}
		}
		for(int i=0;i<t;i++){
			//List li = Arrays.asList(c[i]);
			for(int j=0;j<n[i];j++){
				int k = m[i]-c[i][j];
				if(k>0){
				int key = -1;//Arrays.binarySearch(c[i], j+1, n[i]+1, k);
				for(int l=j+1;l<n[i];l++){
					if(k ==c[i][l]){
						key = l;
						break;
					}
				}
				if(key>=0){
					//System.out.print(m[i] + " ");
					if(j<key){
						System.out.println((j+1) +" "+(key+1));
					}else{
						System.out.println((key+1)+" "+(j+1));
					}
					break;
				}
			}}
		}
		
	}

}
