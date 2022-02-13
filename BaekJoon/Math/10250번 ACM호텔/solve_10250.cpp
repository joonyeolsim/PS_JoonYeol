#include <iostream>
#include <cmath>

using namespace std;


int main() {
    int M, H, W, N;
    int h, w;
    cin >> M;
    int result[M];

    for (int i = 0; i < M; i++) {
        cin >> H >> W >> N;
        w = ceil((double)N / (double)H);
        h = N % H;
        if (h == 0) h = H;
        result[i] = h * 100 + w;
    }

    for (int i = 0; i < M; i++)
        cout << result[i] << endl;

    return 0;
}