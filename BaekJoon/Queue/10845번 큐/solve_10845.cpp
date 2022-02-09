#include <iostream>
#include <queue>

using namespace std;

int main(){
    queue<int> queue;
    int T, value;
    string order;
    cin >> T;

    for (int i=0;i<T;i++) {
        cin >> order;

        if(order=="push"){
            cin >> value;
            queue.push(value);
        }
        else if(order=="pop"){
            if(queue.empty())
                cout << -1 << '\n';
            else{
                cout << queue.front() << '\n';
                queue.pop();
            }
        }
        else if(order=="size")
            cout << queue.size() << '\n';
        else if(order=="empty")
            cout << queue.empty() << '\n';
        else if(order=="front"){
            if(queue.empty())
                cout << -1 << '\n';
            else
                cout << queue.front() << '\n';
        }
        else if(order=="back") {
            if (queue.empty())
                cout << -1 << '\n';
            else
                cout << queue.back() << '\n';
        }
    }
}
