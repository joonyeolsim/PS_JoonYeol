#include <iostream>
#include <vector>

using namespace std;

vector<vector<vector<int>>> dp(51, vector<vector<int>>(51, vector<int>(51, 0)));

int w(int a, int b, int c){
    if (a <= 0 || b <= 0 || c <= 0)
        return dp[0][0][0];
    else if (a > 20 || b > 20 || c > 20){
        if (!dp[20][20][20])
            dp[20][20][20] = w(20, 20, 20);

        return dp[20][20][20];
    }

    else if (a < b && b < c){
        if (!dp[a][b][c-1])
            dp[a][b][c-1] = w(a, b, c-1);

        if (!dp[a][b-1][c-1])
            dp[a][b-1][c-1] = w(a, b-1, c-1);

        if (!dp[a][b-1][c])
            dp[a][b-1][c] = w(a, b-1, c);

        return dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c];
    }

    else{
        if (!dp[a-1][b][c])
            dp[a-1][b][c] = w(a-1, b, c);

        if (!dp[a-1][b-1][c])
            dp[a-1][b-1][c] = w(a-1, b-1, c);

        if (!dp[a-1][b][c-1])
            dp[a-1][b][c-1] = w(a-1, b, c-1);

        if (!dp[a-1][b-1][c-1])
            dp[a-1][b-1][c-1] = w(a-1, b-1, c-1);

        return dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1] ;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    dp[0][0][0] = 1;

    int a, b, c;
    cin >> a >> b >> c;
    while(a != -1 || b != -1 || c != -1){
        cout << "w(" << a << ", " << b << ", " << c << ") = " << w(a, b, c) << '\n';
        cin >> a >> b >> c;
    }
}