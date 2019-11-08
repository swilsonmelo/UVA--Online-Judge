
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static String m;
    public static long[][] dp;

    public static long recu(int i, int j){    	
        if(i > j) return 0;
        if(i == j) return 1;      
        long res = dp[i][j];
        if(res != -1) return res;
        if(m.charAt(i) == m.charAt(j)){   
        	res = 1 + recu(i,j-1) + recu(i+1,j);
        	dp[i][j] = res;
            
        }else{
            res = recu(i,j-1) + recu(i+1,j) - recu(i+1,j-1);
            dp[i][j] = res;
        }
        return res;
    }

    public static void main(String[] args)throws Exception{
        dp = new long[65][65];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cases;
        cases = Integer.parseInt(br.readLine());
        for(int c = 0; c < cases; c++){
            m = br.readLine();                 
            int len = m.length()-1;
            for(int i = 0; i <= len; i++ ) {
            	for(int j = 0; j <= len; j++) {
            		dp[i][j] = -1;
            	}
            }
            long res = recu(0,len);
            System.out.println(res);
        }
    }
}
