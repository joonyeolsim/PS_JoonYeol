#include <iostream>
using namespace std;

int sieve[1000001] = {0, 1};

int main() {
    int M, N;
    cin >> M >> N;

    for (int i = 2; i <= N; i++)
        for (int j = 2; i * j <= N; j++)
            sieve[i * j] = 1;

    for (int i = M; i <= N; i++)
        if(!sieve[i]) cout << i << '\n';

    return 0;
}