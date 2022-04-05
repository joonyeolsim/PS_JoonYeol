#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
<<<<<<< HEAD
    int N, S;
    vector<int> num(100000);
    vector<int> cumulative_sum(100000);
    cin >> N >> S;
    cin >> num[0];
    cumulative_sum[0] = num[0];
    for (int i=1; i<N; i++) {
        cin >> num[i];
        cumulative_sum[i] = num[i-1] + num[i];
    }
    for (int window=0; window<N; window++){
        for (int j=0; j<N-window; j++) {
            if (cumulative_sum[j] - cumulative_sum[j- window - 1] >= S) {
                cout << window;
                return 0;
            }
        }
    }
=======
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
>>>>>>> master
}