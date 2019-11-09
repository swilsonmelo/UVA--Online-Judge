
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;

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
		Collections.sort(dolls, new Comparator<Doll>() {		
			public int compare(Doll d1, Doll d2) {
				if(d1.h == d2.h) {
					if(d1.w < d2.w) {
						return -1;
					}else {
						return 1;
					}
				}
				if( d1.h > d2.h) {
					return -1;
				}else {
					return 1;
				}				
			}			
		});
		/*
		for (int i = 0; i < dolls.size(); i++) {
			System.out.println(dolls.get(i).w + " " + dolls.get(i).h);			
		}
		*/
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
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < n; i++) {
				w = Integer.parseInt(st.nextToken());
				h = Integer.parseInt(st.nextToken());
				Doll doll = new Doll(w, h);
				dolls.add(doll);		
				
			}
			solve();						
		}		
	}		
	public static class Doll{
		public int w;
		public int h;	
		public Doll(int w, int h) {
			this.w = w;
			this.h = h;
		}
	}
}
