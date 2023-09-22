import java.util.Scanner;

class Solution {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int a;
    a = in.nextInt();
    int b; 
    b = in.nextInt();
    System.out.println(solveMeFirst(a, b));
  }
  
  static int solveMeFirst(int a, int b) {
    return a + b;   
  }
}