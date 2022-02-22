#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int num;
    cin >> num;
    for (int i=0; i<num; i++){
        // 별 출력
        for (int j=0; j<=i; j++)
            cout << '*';
        // 띄어쓰기 출력
        for (int j=(num-1)*2; j>i*2; j--)
            cout << ' ';
        // 별 출력
        for (int j=0; j<=i; j++)
            cout << '*';
        cout << '\n';
    }
    for (int i=0; i<num-1; i++){
        for (int j=num-1; j>i; j--)
            cout << '*';
        for (int j=0; j<=i*2+1; j++)
            cout << ' ';
        // 별 출력
        for (int j=num-1; j>i; j--)
            cout << '*';
        cout << '\n';
    }
}