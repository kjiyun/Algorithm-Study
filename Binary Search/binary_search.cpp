// 이진 탐색

/*
    동작 방식

    1. 배열의 중간 값을 가져온다.
    2. 중간 값과 검색 값을 비교한다.
        - 중간 값이 검색 값과 같다면 종료
        - 중간 값보다 검색 값이 크다면 중간 값의 오른쪽 구간을 탐색한다.
        - 중간 값보다 검색 값이 작다면 중간 값의 왼쪽 구간을 탐색한다.
    3. 값을 찾거나 간격이 비어있을 때까지 반복한다.
*/

// 반복문을 이용한 방법
int binarySearch(int arr[], int size, int target) {
    int low = 0;
    int high = size - 1;
    int mid = 0;

    while (low <= high) {
        mid = (low + high) / 2;

        if (target < arr[mid])
            high = mid - 1;
        else if (target > arr[mid])
            low = mid + 1;
        else 
            return mid;  // 반환 값은 인덱스
    }

    return -1;
}


// 재귀 함수를 이용한 방법
