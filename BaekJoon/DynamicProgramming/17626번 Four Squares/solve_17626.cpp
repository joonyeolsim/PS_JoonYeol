#include <bits/stdc++.h>

using namespace std;

int main() {
    int dp[50001];
    dp[1] = 1;
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int num;
    cin >> num;

    for (int i=1; i<=num; i++){
        dp[i] = dp[1] + dp[i-1];
        for (int j=2; j*j<=i; j++)
            dp[i] = min(dp[i], 1 + dp[i-j*j]);
    }
    cout << dp[num] << '\n';
}