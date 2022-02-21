#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    vector<int> day_list = {31,28,31,30,31,30,31,31,30,31,30,31};
    vector<string> week = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"};
    int month, day;
    int day_sum = 0;
    cin >> month >> day;

    for (int i=0; i<month-1; i++)
        day_sum += day_list[i];
    day_sum += day - 1;

    cout << week[day_sum % 7];
}