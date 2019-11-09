
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {

	public static ArrayList<Doll> dolls;
	public static ArrayList<Doll> ans;	
	
	public static int binarySearh(int w) {
		int l = 0;
		int r = ans.size()-1;
		while( l < r ) {
			int mid = (l+r)/2;
			if(ans.get(mid).w <= w) {
				l = mid + 1;
			}else {
				r = mid;
			}
		}
		return l;
	}
	
	public static void solve() {
		/*
		for (int i = 0; i < dolls.size(); i++) {
			System.out.println(dolls.get(i).w + " " + dolls.get(i).h);			
		}
		*/
		//Collections.sort(dolls);
		ans.add(dolls.get(0));
		for (int i = 1; i < dolls.size(); i++) {
			int temp = binarySearh(dolls.get(i).w);
			if(ans.get(temp).w > dolls.get(i).w) {
				ans.get(temp).w = dolls.get(i).w;
			}
			else {
				ans.add(dolls.get(i));
			}								
		}
		System.out.println(ans.size());	
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		ans = new ArrayList<Doll>();
		dolls = new ArrayList<Doll>();
		int cases;
		cases = Integer.parseInt(br.readLine());
		int n, h, w;		
		for (int c = 0; c < cases; c++) {
			ans.clear();
			dolls.clear();
			n = Integer.parseInt(br.readLine());
			String[] line = br.readLine().split(" "); 
			for (int i = 0; i < 2*n; i += 2) {
				//System.out.println(line[i]);
				//w = Integer.parseInt(st.nextToken());
				//h = Integer.parseInt(st.nextToken());
				w = Integer.parseInt(line[i]);
				h = Integer.parseInt(line[i+1]);
				Doll doll = new Doll(w, h);
				dolls.add(doll);		
				
			}
			solve();									
		}				
	}
	
	public static class Doll implements Comparable<Doll> {
		public int w;
		public int h;	
		public Doll(int w, int h) {
			this.w = w;
			this.h = h;
		}

		@Override
		public int compareTo(Doll d) {
			if(this.h == d.h) {
				if(this.w < d.w) {
					return -1;
				}else {
					return 1;
				}
			}
			if( this.h > d.h) {
				return -1;
			}else {
				return 1;
			}				
		}					
	}
}
