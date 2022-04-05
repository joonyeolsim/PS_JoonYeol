#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int N, S, sum = 0, start = 0, end = 0, min_length = 100001;
    cin >> N >> S;
    vector<int> num(N+1);

    for (int i=0; i<N; i++) {
        cin >> num[i];
    }

    while (true) {
        if (sum >= S) {
            if (end - start < min_length) min_length = end - start;
            sum -= num[start];
            start += 1;
        }
        else {
            sum += num[end];
            if (end < N) end += 1;
            else {
                sum -= num[start];
                start += 1;
            }
        }
        if (start >= end) break;
    }
    min_length = min_length == 100001 ? 0 : min_length;
    cout << min_length;
    return 0;
}