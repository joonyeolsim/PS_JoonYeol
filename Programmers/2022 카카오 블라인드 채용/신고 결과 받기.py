def solution(id_list, report, k):
    answer = [0 for _ in id_list]
    reported_count = {user_id: 0 for user_id in id_list}
    user_report_map = {user_id: [] for user_id in id_list}
    suspended_id = []

    for rep in report:
        user_id, report_id = rep.split()
        if report_id not in user_report_map[user_id]:
            user_report_map[user_id].append(report_id)
            reported_count[report_id] += 1
            if reported_count[report_id] == k:
                suspended_id.append(report_id)
    for i, user_id in enumerate(id_list):
        for r_id in user_report_map[user_id]:
            if r_id in suspended_id:
                answer[i] += 1
    return answer


if __name__ == '__main__':
    print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))