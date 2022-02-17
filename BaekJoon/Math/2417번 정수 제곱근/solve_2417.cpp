#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cout.setf(ios::fixed);

    long num;
    cin >> num;
    cout << setprecision(0) << ceil(sqrt(num)) <<  '\n';
}