#include <iostream>

using namespace std;

int main() {
    int A, B, C;
    cin >> A >> B;
    cin >> C;

    B += C;

    while (B >= 60){
        B -= 60;
        if (A == 23)
            A = 0;
        else
            A += 1;
    }


    cout << A << " " << B << endl;
}