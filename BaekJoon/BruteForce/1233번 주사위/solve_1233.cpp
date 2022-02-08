#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int dice1, dice2, dice3;
    cin >> dice1 >> dice2 >> dice3;

    int sum[80] = {0,};

    for (int i=1; i<=dice1; i++)
        for (int j=1; j<=dice2; j++)
            for (int k=1; k<=dice3; k++)
                sum[i+j+k] += 1;

    cout << distance(sum, std::max_element(sum, sum+80)) << "\n";
}