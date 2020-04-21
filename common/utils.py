def compare_version(v1, v2):
    v1_arr = v1.split(".")
    v2_arr = v2.split(".")

    if v1_arr[0] > v2_arr[0]:
        return 1
    elif v1_arr[0] < v2_arr[0]:
        return -1
    else:
        v1_left = v1_arr[1:]
        v2_left = v2_arr[1:]

        v1_left_len = len(v1_left)
        v2_left_len = len(v2_left)

        if v1_left_len > v2_left_len:
            for i in range(v1_left_len - v2_left_len):
                v2_left.append("0")
        else:
            for i in range(v2_left_len - v1_left_len):
                v1_left.append("0")

        # print(v1, v2, v1_left, v2_left)
        v1_left_value = int(''.join(v1_left))
        v2_left_value = int(''.join(v2_left))
        if v1_left_value > v2_left_value:
            return 1
        elif v1_left_value < v2_left_value:
            return -1
        else:
            return 0
