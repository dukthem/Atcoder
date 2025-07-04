#include<iostream>
#include<vector>
using namespace std;

int main() {
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    
    int N;
    cin >> N;
    int numbers;
    for (int i = 0; i < N; ++i) {
        cin >> numbers;
        cout << numbers;
    }
    
    
    return 0;
}