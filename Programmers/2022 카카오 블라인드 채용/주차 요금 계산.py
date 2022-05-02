import math


def solution(fees, records):
    answer = []
    car_in_time_dict = {}
    car_open_set_dict = {}
    total_time_dict = {}
    for record in records:
        str_time, car_n, method = record.split()
        if car_n not in total_time_dict.keys():
            total_time_dict[car_n] = 0
        hour, minute = map(int, str_time.split(":"))
        time = hour * 60 + minute
        if method == "IN":
            car_open_set_dict[car_n] = "IN"
            car_in_time_dict[car_n] = time
        else:
            car_open_set_dict[car_n] = "OUT"
            total_time_dict[car_n] += time - car_in_time_dict[car_n]

    for car_n in sorted(car_open_set_dict.keys()):
        if car_open_set_dict[car_n] == "IN":
            total_time_dict[car_n] += 23 * 60 + 59 - car_in_time_dict[car_n]

        if total_time_dict[car_n] < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((total_time_dict[car_n] - fees[0]) / fees[2]) * fees[3])
    return answer


if __name__ == '__main__':
    print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))