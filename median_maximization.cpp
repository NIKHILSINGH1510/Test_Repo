#include <bits/stdc++.h>
using namespace std;
int main()
{
    long int r;
    cin >> r;
    while (r--)
    {
        long long int n, s, p;
        cin >> n >> s;
        p = (n / 2) + 1;
        cout << s / p << endl;
    }
}