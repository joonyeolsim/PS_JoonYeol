#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> adj_list(100001);
bool visited[100001];
int this_cnt;

void dfs(int current_node){
    this_cnt++;
    visited[current_node] = true;
    for (const int &next_node : adj_list[current_node])
        if (!visited[next_node])
            dfs(next_node);
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N, M;
    int max_cnt = -1;
    vector<int> result;
    cin >> N >> M;

    for (int i=0;i<M;i++){
        int u, v;
        cin >> u >> v;
        adj_list[v].push_back(u);
    }

    for (int i=1;i<=N;i++){
        memset(visited, false, N + 1);
        this_cnt = 0;
        dfs(i);
        if (this_cnt > max_cnt){
            result.clear();
            result.push_back(i);
            max_cnt = this_cnt;
        }
        else if (this_cnt == max_cnt)
            result.push_back(i);
    }

    for (const int &num : result)
        cout << num << " ";
    return 0;
}