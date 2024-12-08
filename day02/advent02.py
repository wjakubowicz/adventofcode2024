def is_safe_report(report):
    increasing = all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def is_safe_with_dampener(report):
    if is_safe_report(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    return False

def count_safe_reports(data):
    reports = [list(map(int, line.split())) for line in data.strip().split('\n')]
    safe_count = sum(1 for report in reports if is_safe_with_dampener(report))
    return safe_count

if __name__ == '__main__':
    with open('advent02.txt', 'r') as file:
        data = file.read()

    safe_reports_count = count_safe_reports(data)
    print(f"Number of safe reports: {safe_reports_count}")