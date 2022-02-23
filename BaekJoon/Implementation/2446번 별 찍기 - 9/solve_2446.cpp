#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int num;
    cin >> num;

    for (int i=0; i<num; i++){
        for (int j=0; j<i; j++){
            cout << ' ';
        }
        for (int j=num*2-1; j>i*2; j--){
            cout << '*';
        }
        cout << '\n';
    }

    for (int i=num-1; i>0; i--){
        for (int j=(i-1); j>0; j--){
            cout << ' ';
        }
        for (int j=(i-1)*2; j<num*2-1; j++){
            cout << '*';
        }
        cout << '\n';
    }
}