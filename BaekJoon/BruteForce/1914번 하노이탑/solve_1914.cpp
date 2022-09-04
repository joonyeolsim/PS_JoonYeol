#include <iostream>
#include <cmath>

using namespace std;


void hanoi(int n, int from, int by, int to){
    if (n == 0)
        return;
    hanoi(n - 1, from, to, by);
    cout << from << " " << to << "\n";
    hanoi(n - 1, by, from, to);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N;
    cin >> N;

    string s = to_string(pow(2, N));

    int x = s.find('.');				//pow 함수 결과가 실수형이기에 소수점 찾기
    s = s.substr(0, x);				//소수점 앞자리만 나오게하기
    s[s.length() - 1] -= 1;

    cout << s << "\n";

    if (N <= 20){
        hanoi(N, 1, 2, 3);
    }
}