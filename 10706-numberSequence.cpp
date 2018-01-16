#include <bits/stdc++.h>
using namespace std;
  
int digit(int n) {
  int d = 0;
  while (n) {
    n /= 10;
    d++;
  }
  return d;
}
 
int digitOf(int n, int pos) {
  char s[99];
  sprintf(s, "%d", n);
  return s[pos - 1] - '0';
}
 
int main() {
  long long sum[40000], len[40000];
  for (long long i = 1, j = 0; j < 2147483647; i++) {
    len[i] = digit(i);
    sum[i] = sum[i - 1] + len[i];
    j += sum[i];
  }
  int T;
  scanf("%d", &T);
  while (T--) {
    int n;
    scanf("%d", &n);
    for (int i = 0; n > sum[i]; n -= sum[i++]);
    int num;
    for (num = 1; n > len[num]; n -= len[num++]);
    printf("%d\n", digitOf(num, n));
  }
  return 0;
}
