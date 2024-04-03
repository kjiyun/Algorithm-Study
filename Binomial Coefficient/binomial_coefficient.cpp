#include <iostream>
#include <algorithm>
using namespace std;

// Divide and Conquer 이용
int bin_recursion(int n, int k){
    if ((k==0) || (k==n)){
        return 1;
    }
    else {
        return bin_recursion(n-1, k-1) + bin_recursion(n-1, k);
        // 분할된 크기가 원래의 instance와 비슷하므로 비효율적임
    }
}


// DP 이용
int arr[100][100] = {0, };

int bin_dp(int n, int k){
    for (int i=0; i<=n; i++){
        for (int j=0; j<=min(k, i); j++){
            if ((j==0) || (j==i)) {
                arr[i][j] = i;
            }
            else {
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j];
            }
        }
    }
    return arr[n][k];
}