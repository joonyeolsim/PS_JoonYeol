#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(int a, int b){
    return a > b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    vector<int> ropes;
    int N, num, weight, max_weight = 0;
    cin >> N;

    for (int i = 0; i < N; i++){
        cin >> num;
        ropes.push_back(num);
    }
    sort(ropes.begin(), ropes.end(), compare);

    for (int j = 0; j < N; j++){
        weight = ropes[j];
        max_weight = max(weight * (j+1), max_weight);
    }
    cout << max_weight;
}