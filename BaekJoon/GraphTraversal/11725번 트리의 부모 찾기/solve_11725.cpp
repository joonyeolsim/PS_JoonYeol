#include <bits/stdc++.h>

using namespace std;

int visited[100005];
vector<vector<int>> adj_list(100005);
int result[100005];

void dfs(int current_node){
    for (const int &node: adj_list[current_node]){
        if (visited[node] == 0){
            visited[node] = 1;
            result[node] = current_node;
            dfs(node);
        }
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 0; i < N - 1; i++){
        int node1, node2;
        cin >> node1 >> node2;
        adj_list[node1].push_back(node2);
        adj_list[node2].push_back(node1);
    }
    dfs(1);
    for (int i = 2; i <= N; i++)
        cout << result[i] << '\n';
    return 0;
}