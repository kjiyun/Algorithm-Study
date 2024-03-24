# 참고: http://bigdata.dongguk.ac.kr/lectures/Python/_book/numpy.html
import numpy as np

def strassen(matrix1, matrix2):
    n = len(matrix1)

    if n == 1:
        return matrix1 * matrix2
    
    new_size = n // 2

    # 행렬을 4개의 부분 행렬로 분할한다
    a11 = matrix1[:new_size, :new_size]
    a12 = matrix1[:new_size, new_size:]
    a21 = matrix1[new_size:, :new_size]
    a22 = matrix1[new_size:, new_size:]

    b11 = matrix2[:new_size, :new_size]
    b12 = matrix2[:new_size, new_size:]
    b21 = matrix2[new_size:, :new_size]
    b22 = matrix2[new_size:, new_size:]

    # 슈트라센의 행렬 곱셈 알고리즘을 재귀적으로 호출한다
    m1 = strassen(a11 + a22, b11 + b22)
    m2 = strassen(a21 + a22, b11)
    m3 = strassen(a11, b12 - b22)
    m4 = strassen(a22, b21 - b11)
    m5 = strassen(a11 + a12, b22)
    m6 = strassen(a21 - a11, b11 + b12)
    m7 = strassen(a12 - a22, b21 + b22)

    # 결과 행렬을 생성한다
    c11 = m1 + m4 - m5 + m7
    c12 = m3 + m5
    c21 = m2 + m4
    c22 = m1 - m2 + m3 + m6

    # 분할된 부분 행렬들을 합쳐서 결과 행렬을 반환한다
    return np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    """
    참고: Numpy의 hstack, vstack 메서드
    hstack의 h는 horisontal, 즉 수평이라는 뜻으로 hstack을 사용하면 가로로 행렬 결합이 이루어진다.
    vstack의 v는 vertical, 수직이라는 뜻으로 vstack을 사용하면 수직으로 행렬 결합이 이루어진다.
    위의 코드는 1행에 c11, c12, 2행에 c21, c22가 존재하도록 하는 코드이다.
    """

# matrix 행렬을 생성한다
matrix1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
matrix2 = np.array([[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]])

# 슈트라센의 행렬 곱셈 알고리즘을 사용하여 두 행렬을 곱한다
result = strassen(matrix1, matrix2)

# 결과 출력
print(result)