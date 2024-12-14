def is_safe_report(report):
    diffs = [b - a for a, b in zip(report, report[1:])]
    return all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs)

def is_safe_with_dampener(report):
    return any(is_safe_report(report[:i] + report[i + 1:]) for i in range(len(report)))

def count_safe_reports(data):
    reports = [list(map(int, line.split())) for line in data.strip().split('\n')]
    part1_safe_count = sum(is_safe_report(report) for report in reports)
    part2_safe_count = sum(is_safe_with_dampener(report) for report in reports)
    return part1_safe_count, part2_safe_count

if __name__ == '__main__':
    with open('advent02.txt', 'r') as file:
        data = file.read()
    safe_reports_part1, safe_reports_part2 = count_safe_reports(data)
    print(f"Part 1 - Number of safe reports: {safe_reports_part1}")
    print(f"Part 2 - Number of safe reports with dampener: {safe_reports_part2}")