if __name__ == '__main__':
    iron_input = input()
    last_input = ""
    truncated_iron_list = []
    piece = 0
    new_iron = 0

    for ch in iron_input:
        # 레이저일때
        if last_input == "(" and ch == ")":
            # 방금 전꺼는 레이저의 일부분이었으니까 삭제
            truncated_iron_list.pop()
            new_iron -= 1

            if truncated_iron_list:
                piece += len(truncated_iron_list)
                if new_iron:
                    for i, _ in enumerate(truncated_iron_list[-new_iron:]):
                        if truncated_iron_list[-new_iron+i] == 0:
                            piece += 1
                            truncated_iron_list[i] = 1
                    new_iron = 0

        # 레이저가 아니라 쇠막대기의 끝일때
        elif last_input == ")" and ch == ")":
            truncated_iron_list.pop()

        # 쇠막대기 시작일때
        else:
            truncated_iron_list.append(0)
            new_iron += 1
        last_input = ch
    print(piece)
