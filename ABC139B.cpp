#include<iostream>
using namespace std;

int main() {
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int A, B;
    int ans = 1;
    cin >> A >> B;
    int a = A;
    if ((A == 0) || (B == 0)) {
        cout << 0;
    }
    else if (A >= B) {
        cout << 1;
    } else {
        while(A < B) {
            A += a;
            ans += 1;
        }
        cout << ans;

    }
    

    
    
    return 0;
}