#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    int* wages = new int[n];
    long max_sum = 0;
    long sum = 0;

    for (int i=0; i<n; i++)
        cin >> wages[i];

    for (int i=0; i<m; i++)
        sum += wages[i];

    max_sum = sum;

    for (int i=1; i<n-m+1; i++){
        sum -= wages[i-1];
        sum += wages[i+m-1];
        if (sum > max_sum) max_sum = sum;
    }

    cout << max_sum;
}