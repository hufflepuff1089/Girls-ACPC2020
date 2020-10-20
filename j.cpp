#include <bits/stdc++.h>
using namespace std;

int b_pref[100001];
int a[100001], b[100001];

int sum_b(int start, int end)
{
    if(end < start) return 0;
    if(start > 0) return sum_b(0, end) - sum_b(0, start - 1);
    return b_pref[end];
}

int main()
{
    auto in = ifstream("rapunzel.in");

    int T;
    in >> T;
    while(T--)
    {
        int N, K, L;
        in >> N >> K >> L;
        for(int i = 0; i < N; i++) in >> a[i];
        for(int i = 0; i < N; i++) in >> b[i];

        b_pref[0] = b[0];
        for(int i = 1; i < N; i++)
            b_pref[i] = b_pref[i-1] + b[i];
        
        int best = -1;

        for(int i = 0; i < N; i++)
        {
            if(best != -1) break;

            int lo = i, hi = N;
            while(lo < hi)
            {
                int mid = (lo + hi) / 2;
                int x = L * a[i] + sum_b(i+1, mid);

                if(x >= K - 1 && x <= K + 1)
                {
                    best = i+1;
                    break;
                }

                if(x > K+1) hi = mid;
                else if(x < K-1) lo = mid+1;
            }
        }

        cout << best << endl;
    }
}
