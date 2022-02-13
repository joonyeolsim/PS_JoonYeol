#include <iostream>

using namespace std;

int main(){
    int num[5], sum=0;
    cin >> num[0] >> num[1] >> num[2] >> num[3] >> num[4];

    for (int i : num)
        sum += i * i;
    cout << sum % 10;
}