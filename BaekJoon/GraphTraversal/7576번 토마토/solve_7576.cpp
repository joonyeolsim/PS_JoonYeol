#include <vector>
#include <iostream>
#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int M, N, tomato;
    cin >> M >> N;

    vector<vector<int>> tomato_box(N, vector<int>(M, 0));
    vector<vector<int>> visited(N, vector<int>(M, 0));
    vector<pair<int, int>> direction = {
            pair<int, int>(0, 1),
            pair<int, int>(1, 0),
            pair<int, int>(0, -1),
            pair<int, int>(-1, 0),
    };

    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            cin >> tomato;
            tomato_box[i][j] = tomato;
        }
    }

    deque<pair<int, int>> open_set;
    int tomato_n = 0;
    int next_tomato_n = 0;
    int day = -1;
    for (int i=0; i<N; i++){
        for (int j=0; j<M; j++){
            if (tomato_box[i][j] == 1 && !visited[i][j]){
                open_set.emplace_back(i, j);
                tomato_n++;
            }
        }
    }

    while(!open_set.empty()) {
        while (tomato_n--) {
            int y = open_set[0].first;
            int x = open_set[0].second;
            visited[y][x] = 1;
            open_set.pop_front();

            for (auto d: direction) {
                int next_y = y + d.first;
                int next_x = x + d.second;
                if (0 <= next_y && next_y < N && 0 <= next_x && next_x < M) {
                    if (tomato_box[next_y][next_x] == 0 && !visited[next_y][next_x]) {
                        tomato_box[next_y][next_x] = 1;
                        open_set.emplace_back(next_y, next_x);
                        next_tomato_n++;
                    }
                }
            }
        }
        tomato_n = next_tomato_n;
        next_tomato_n = 0;
        day++;
    }

    // 마지막 확인
    for (int i=0; i<N; i++){
        for (int j=0; j<M; j++){
            if (tomato_box[i][j] == 0)
                day = -1;
        }
    }

    cout << day << '\n';
}
