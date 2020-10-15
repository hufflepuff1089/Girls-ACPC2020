#include <bits/stdc++.h>
using namespace std;

set<string> nodes;
map<string, vector<string>> G;
map<string, int> comp;

void connect(string u, int c)
{
    if(comp[u] != -1) return;
    comp[u] = c;
    for(string v : G[u])
        connect(v, c);
}

short memo[501][501][501];
vector<int> vals;

int calc(int m1, int m2, int i)
{
    if(i >= vals.size()) return 0;

    if(memo[m1][m2][i] != -1) return memo[m1][m2][i];

    int res = calc(m1, m2, i+1) + vals[i];
    if(m1 - vals[i] >= 0)
        res = min(res, calc(m1-vals[i], m2, i+1));
    if(m2 - vals[i] >= 0)
        res = min(res, calc(m1, m2-vals[i], i+1));
    
    memo[m1][m2][i] = res;
    return res;
}

int main()
{
    auto in = ifstream("land.in");

    int T;
    in >> T;

    while(T--)
    {
        G.clear();
        nodes.clear();
        comp.clear();
        vals.clear();

        int n, m1, m2;
        in >> n >> m1 >> m2;
        
        for(int i = 0; i < n; i++)
        {
            string a, b;
            in >> a >> b;
            G[a].push_back(b);
            G[b].push_back(a);

            nodes.insert(a);
            nodes.insert(b);
        }

        int i = 0;
        for(string u : nodes) comp[u] = -1;
        for(string u : nodes) connect(u, i++);

        vector<int> comp_size(nodes.size(), 0);
        for(string u : nodes) comp_size[comp[u]]++;

        for(int i = 0; i < comp_size.size(); i++)
            if(comp_size[i] > 0)
                vals.push_back(comp_size[i]);
        
        for(int i = 0; i < m1+1; i++)
            for(int j = 0; j < m2+1; j++)
                for(int k = 0; k < comp_size.size()+1; k++)
                    memo[i][j][k] = -1;

        
        cout << calc(m1, m2, 0) << endl;
    }
}
