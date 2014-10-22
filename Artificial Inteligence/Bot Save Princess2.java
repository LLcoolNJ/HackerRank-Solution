import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
static void nextMove(int n, int r, int c, String [] grid){
  
  int b_xpos = c, b_ypos = r, p_xpos = -1, p_ypos = -1;
	for(int i=0;i<n;i++){
		if(grid[i].indexOf('p')>-1){
			p_ypos = i;
			p_xpos = grid[i].indexOf('p');
		}
		if(p_xpos>=0 && p_ypos>=0){
			break;
		}
	}
	boolean flag = true;
		if(b_xpos > p_xpos){
			b_xpos--;
			flag = false;
			System.out.println("LEFT");
		}else if(b_xpos < p_xpos){
			b_xpos++;
			flag = false;
			System.out.println("RIGHT");
		}
		if(b_ypos > p_ypos && flag == true){
			b_ypos--;
			System.out.println("UP");
		}else if(b_ypos < p_ypos && flag == true){
			b_ypos++;
			System.out.println("DOWN");
		}
	
  }
public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n,r,c;
        n = in.nextInt();
        r = in.nextInt();
        c = in.nextInt();
        in.useDelimiter("\n");
        String grid[] = new String[n];


        for(int i = 0; i < n; i++) {
            grid[i] = in.next();
        }

    nextMove(n,r,c,grid);

    }
}
