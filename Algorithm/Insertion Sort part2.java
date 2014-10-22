import java.io.*;
import java.util.*;

public class Solution {

    public static void insertionSortPart2(int[] ar, int s)
    {       
           // Fill up the code for the required logic here
           // Manipulate the array as required
           // The code for Input/Output is already provided
      	for(int i=0;i<s-1;i++){
          int j = i+1;
          while(j>0){
            if(ar[j]<ar[j-1]){
              int temp = ar[j];
              ar[j] = ar[j-1];
              ar[j-1] = temp;
              j--;
            }else{
            	break;
            }
          }
          printArray(ar);
        }
    }  
    
    
      
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
       int s = in.nextInt();
       int[] ar = new int[s];
       for(int i=0;i<s;i++){
            ar[i]=in.nextInt(); 
       }
       insertionSortPart2(ar,s);
       //printArray(ar);
                    
    }    
    private static void printArray(int[] ar) {
      for(int n: ar){
         System.out.print(n+" ");
      }
        System.out.println("");
   }
}
