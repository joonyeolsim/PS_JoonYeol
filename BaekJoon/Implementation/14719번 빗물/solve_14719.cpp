#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int width, height, block;
    cin >> height >> width;
    vector<vector<int>> grid(height, vector<int>(width, 0));
    
    // i가 width j가 height
    for (int i=0; i<width; i++){
        cin >> block;
        for (int j=0; j<block; j++)
            grid[j][i] = 1;
    }

    for (int h=0; h<height; h++) {
        for (int w=0; w<width; w++) {
            if (grid[h][w] == 0){
                // 빗물이 흘러 가는 걸 구현
                int right_w = w + 1;
                int left_w = w - 1;
                bool go_right = true;
                bool go_left = true;
                bool right_wall = false;
                bool left_wall = false;
                while (go_right || go_left){
                    if (right_w < width) {
                        if (grid[h][right_w] == 1){
                            go_right = false;
                            right_wall = true;
                        }
                        else{
                            right_w += 1;
                        }
                    }
                    else {
                        go_right = false;
                    }
                    if (left_w >= 0) {
                        if (grid[h][left_w] == 1) {
                            go_left = false;
                            left_wall = true;
                        } else {
                            left_w -= 1;
                        }
                    }
                    else {
                        go_left = false;
                    }
                }
                if (right_wall && left_wall)
                    grid[h][w] = 2;
            }
        }
    }
    int rain_sum = 0;

    for (int h = 0; h < height; h++) {
        for (int w = 0; w < width; w++) {
            if (grid[h][w] == 2)
                rain_sum += 1;
        }
    }

    cout << rain_sum << endl;
}