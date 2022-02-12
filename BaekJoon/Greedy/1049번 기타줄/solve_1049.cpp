#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int N, M, package_price, piece_price;
    cin >> N >> M;
    double min_price = 1001 * N;
    int min_package_price = 1001, min_piece_price = 1001;
    int package_num, piece_num;

    for(int i=0; i<M; i++){
        cin >> package_price >> piece_price;
        if (package_price < min_package_price)
            min_package_price = package_price;
        if (piece_price < min_piece_price)
            min_piece_price = piece_price;
    }

    // 패키지만으로 사기
    package_num = ceil(N / 6.0);
    if(package_num * min_package_price < min_price)
        min_price = package_num * min_package_price;

    // 패키지 + 낱개
    package_num = floor(N / 6.0);
    piece_num = N % 6;
    if(package_num * min_package_price + piece_num * min_piece_price < min_price)
        min_price = package_num * min_package_price + piece_num * min_piece_price;

    // 낱개만으로 사기
    if(min_piece_price * N < min_price)
        min_price = min_piece_price * N;

    cout << min_price << endl;
}