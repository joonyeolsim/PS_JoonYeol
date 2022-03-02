#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    vector<int> dp;
    int X;
    // 초기화
    dp.push_back(0);
    dp.push_back(0);

    cin >> X;
    for (int i = 2; i <= X; i++) {
        dp.push_back(dp[i - 1] + 1);
        if (i % 3 == 0)
            dp[i] = min(dp[i], dp[i / 3] + 1);
        if (i % 2 == 0)
            dp[i] = min(dp[i], dp[i / 2] + 1);
    }

    cout << dp[X];
}