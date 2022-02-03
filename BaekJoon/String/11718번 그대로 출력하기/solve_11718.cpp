#include <iostream>

using namespace std;

int main() {
    string sentence;
    while(true){
        getline(cin, sentence);
        if(sentence.empty())
            break;
        cout << sentence << endl;
    }
}