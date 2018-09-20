package maraton;

import java.io.*;

public class ModularFibonacci10229 {
 
    public static long [][] getMatrixMult(long[][] mat1, long [][] mat2,long m){
        long [][] res = new long [mat1.length][mat2[0].length];
        //System.out.println("mat1 "+mat1.length+" "+mat1[0].length);
        //System.out.println("mat2 "+mat2.length+" "+mat2[0].length);
        //System.out.println(res[0][0]);
        for (int i = 0; i < mat1.length; i++) {
            for (int j = 0; j < mat2[0].length; j++) {
                for (int k = 0; k < mat1[0].length; k++) {
                	/*System.out.println(mat1.length+" "+mat2[0].length+" "+mat1[0].length
                			+" "+i+" "+j+" "+k);*/
                    res[i][j] =(res[i][j]+  mat1[i][k] * mat2[k][j]) % m;
                }
            }
        }
        return res;
    }
     
    public static long[][] getModExp(long [][] mat, long p, long m){
        long[][] res = new long [mat.length][mat[0].length];
        
        int counter = 0;
        while(p > 0){
        	//System.out.println(mat.length +" "+mat[0].length);
            if(p%2 == 1){
                if(counter++ == 0){                	
                	//System.out.println(counter + " kha");
                    res = mat;
                }
                else
                    res = getMatrixMult(mat,res,m);
                
            }
            p = p >> 1;
            mat = getMatrixMult(mat, mat,m);
        }
        return res;
    }
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String newLine = in.readLine();
        String[] sp ;
        int n , m;
        while(newLine != null){
            long [][] T = {{1,1},{1,0}};
            long [][] F = {{1},{1}};
            sp = newLine.split(" ");
            n = Integer.parseInt(sp[0]);
            m = (int) Math.pow(2, Integer.parseInt(sp[1]));
            //System.out.println(n+" "+m);
            if(n == 0)
                System.out.println(0);
            else if(n==1 || n ==2)
                System.out.println(1);
            else{
                T = getModExp(T, n-2, m);
                F = getMatrixMult(T, F,m);
                System.out.println(F[0][0]);
            }
            newLine = in.readLine();
        }
    }
 
}