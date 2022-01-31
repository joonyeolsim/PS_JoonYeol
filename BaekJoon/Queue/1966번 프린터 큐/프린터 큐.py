from collections import deque

if __name__ == '__main__':
    test_case = int(input())
    result = []
    for _ in range(test_case):
        cnt = 0
        finding_flag = False
        document_num, find_document_num = map(int, input().split())
        p_list = list(map(int, input().split()))
        priority_queue = deque(sorted(p_list, reverse=True))
        document_queue = deque([i, p] for i, p in enumerate(p_list))
        while not finding_flag:
            cur_priority = priority_queue.popleft()
            while True:
                this_document = document_queue.popleft()
                if this_document[1] == cur_priority:
                    if this_document[0] == find_document_num:
                        finding_flag = True
                    cnt += 1
                    break
                else:
                    document_queue.append(this_document)
        result.append(cnt)
    for data in result:
        print(data)



