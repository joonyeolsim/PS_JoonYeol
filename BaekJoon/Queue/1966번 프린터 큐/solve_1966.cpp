#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int T, N, M, num, next_max, index;
    deque<pair<int, int>> importance;

    cin >> T;
    while(T--){
        cin >> N >> M;

        for(int i=0; i<N; i++){
            cin >> num;
            importance.emplace_back(num, i);
        }

        index = 1;
        next_max = max_element(importance.begin(), importance.end())->first;
        while(!importance.empty()){
            if (importance[0].first == next_max){
                if (importance[0].second == M){
                    cout << index << '\n';
                    break;
                }
                importance.pop_front();
                next_max = max_element(importance.begin(), importance.end())->first;
                index++;
            }
            else{
                importance.push_back(importance[0]);
                importance.pop_front();
            }
        }

        importance.clear();
    }
}