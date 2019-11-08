

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static long[] fib;
	
	public static void preCalc() {
		fib[0] = 1;
		fib[1] = 2;
		for (int i = 2; i < fib.length; i++) {
			fib[i] = fib[i-1] + fib[i-2];
		}
	}	
	public static void solve(int n) {
		System.out.print(n + " = ");
		String res = "";
		boolean flag = false;
		for (int i = fib.length-1; i >= 0; i--){
			if(fib[i] <= n) {
				flag = true;
				res += "1";
				n -= fib[i];
			}else if(flag) {
				res += "0";
			}
			
		}
		System.out.print(res + " (fib)");
		System.out.println();				
	}
	public static void main(String[] args) throws Exception {
		fib = new long[40];
		preCalc();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cases;
		int n;
		cases = Integer.parseInt(br.readLine());
		for (int c = 0; c < cases; c++) {
			n = Integer.parseInt(br.readLine());
			solve(n);
		}
	}
	
}
