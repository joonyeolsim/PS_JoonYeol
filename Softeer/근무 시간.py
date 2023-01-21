import sys
from datetime import timedelta


if __name__ == '__main__':
    result = timedelta()

    for _ in range(5):
        start_work, end_work = sys.stdin.readline().split()
        start_hour, start_minute = map(int, start_work.split(':'))
        end_hour, end_minute = map(int, end_work.split(':'))

        start_time = timedelta(hours=start_hour, minutes=start_minute)
        end_time = timedelta(hours=end_hour, minutes=end_minute)
        result += end_time - start_time

    print(int(result.total_seconds() / 60))