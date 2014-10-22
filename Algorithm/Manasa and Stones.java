import java.util.Scanner;


public class Solution {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int t = in.nextInt();
		int n[] = new int[t];
		int a[] = new int[t];
		int b[] = new int[t];
		for(int i=0;i<t;i++){
			n[i] = in.nextInt();
			a[i] = in.nextInt();
			b[i] = in.nextInt();
		}
		int li[][] = new int[t][1000];
		for(int i=0;i<t;i++){
			if(a[i]<b[i]){
				for(int j=0;j<n[i];j++){
					li[i][j] = (n[i] - 1 - j)*a[i] + j*b[i];
				}
			}else if(a[i]>b[i]){
				for(int j=0;j<n[i];j++){
					li[i][j] = (n[i] - 1 - j)*b[i] + j*a[i];
				}
			}else{
				li[i][0] = (n[i] - 1)*b[i];
				n[i] = 1;
			}
			
		}
		for(int i=0;i<t;i++){
			for(int j=0;j<n[i];j++){
				System.out.print(li[i][j] + " ");
			}
			System.out.print("\n");
		}

	}

}
