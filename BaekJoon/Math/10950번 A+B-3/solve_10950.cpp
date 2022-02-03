//
// Created by ventu on 2022-02-01.
//


#include <iostream>

using namespace std;

int main() {
    int N, num1, num2;
    cin >> N;

    for (int i = 0; i < N; i++){
        cin >> num1 >> num2;
        cout << num1 + num2 << endl;
    }
}