#include <bits/stdc++.h>
using namespace std;

long long gcd(int a, int b)
{
    if(b == 0) return a;
    return gcd(b, a % b);
}

long long alg(int m, int h)
{
    long long d = gcd(m, h);
    m /= d;
    h /= d;
    return m + h;
}

long long tab[1001][1001];

int main()
{
    auto in = ifstream("cat.in");
    long long T, nc, m;

    in >> T;
    while(T--)
    {
        in >> nc >> m;

        for(int i = 0; i < 1001; i++)
            for(int j = 0; j < 1001; j++)
                tab[i][j] = -1;
        
        tab[0][m] = 0;

        for(int i = 0; i < nc; i++)
        {
            long long h, e;
            in >> h >> e;

            for(int j = 0; j < 1000; j++)
            {
                if(tab[i][j] != -1)
                {
                    if(tab[i+1][j] == -1) tab[i+1][j] = tab[i][j];
                    else tab[i+1][j] = min(tab[i+1][j], tab[i][j]);
                }
                
                if(tab[i][j] == -1) continue;

                long long newh = alg(j, h);
                if(newh >= 1000) continue;
                
                if((tab[i+1][newh] == -1) || (tab[i+1][newh] > tab[i][j] + e))
                {
                    tab[i+1][newh] = tab[i][j] + e;
                }
            }
        }

        long long res = -1;
        for(int i = 0; i < 3; i++)
        {
            if(tab[nc][i] != -1)
            {
                if(res == -1) res = tab[nc][i];
                else res = min(res, tab[nc][i]);
            }
        }

        cout << res << endl;
    }
}
