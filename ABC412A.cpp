#include<iostream>
using namespace std;

int main() {
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    //     freopen("output.txt", "w", stdout);
    // #endif
    int N;
    cin >> N;
    int ans = 0;
    int A, B;
    for (int i = 1; i <= N; ++i) {
        cin >>A>>B;
        if (B > A) {
            ans += 1;
        }
    }
    cout << ans;
    
    return 0;
}