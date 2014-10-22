import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
static void displayPathtoPrincess(int n, String [] grid){
  int b_xpos = -1, b_ypos = -1, p_xpos = -1, p_ypos = -1;
	for(int i=0;i<n;i++){
		if(grid[i].indexOf('p')>-1){
			p_ypos = i;
			p_xpos = grid[i].indexOf('p');
		}
		if(grid[i].indexOf('m')>-1){
			b_ypos = i;
			b_xpos = grid[i].indexOf('m');
		}
		if(b_xpos >=0 && b_ypos >=0 && p_xpos>=0 && p_ypos>=0){
			break;
		}
	}
	while(b_xpos != p_xpos || b_ypos != p_ypos){
		if(b_xpos > p_xpos){
			b_xpos--;
			System.out.println("LEFT");
		}else if(b_xpos < p_xpos){
			b_xpos++;
			System.out.println("RIGHT");
		}
		if(b_ypos > p_ypos){
			b_ypos--;
			System.out.println("UP");
		}else if(b_ypos < p_ypos){
			b_ypos++;
			System.out.println("DOWN");
		}
	}
  
  }
public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m;
        m = in.nextInt();
        String grid[] = new String[m];
        for(int i = 0; i < m; i++) {
            grid[i] = in.next();
        }

    displayPathtoPrincess(m,grid);
    }
}
