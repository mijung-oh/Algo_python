def solution(arr1, arr2):
    # axb bxc => axc
    r_len = len(arr1)
    c_len = len(arr2[0])

    new_arr = [[0 for _ in range(c_len)] for _ in range(r_len)]

    # i: 왼쪽행렬 행 idx
    for i in range(r_len):
        # 가로 행
        r = arr1[i]
        # 0 1 2
        # k: 오른쪽 행렬 열 idx
        for k in range(c_len):
            # 세로 열
            c = []
            # 두번째 행렬 행 idx
            for j in range(len(arr2)):
                c.append(arr2[j][k])
            sub_sum = 0
            # 두 배열 곱하기
            for j in range(len(r)):
                sub_sum += r[j] * c[j]
            new_arr[i][k] = sub_sum
    return new_arr
solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]	)