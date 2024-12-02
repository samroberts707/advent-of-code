with open ('input.txt', 'r') as _file:
    reports = [entry.rstrip() for entry in _file]

safe_reports = 0

for report in reports:
    report_safe = True
    last_level = 0
    report = report.split(' ')
    # Ascending Check
    if int(report[0]) < int(report[1]):
        for level in range(len(report)):
            if level != 0:
                # print("Comparing", report[level], "with last level of:", last_level)
                if int(report[level]) > last_level and int(report[level]) < last_level+4:
                    # print("Safe level")
                    pass
                else: 
                    report_safe = False
                    # print("Unsafe level")
                last_level = int(report[level])
            else:
                last_level = int(report[level])
    else:
        for level in range(len(report)):
            if level != 0:
                # print("Comparing", report[level], "with last level of:", last_level)
                if int(report[level]) < last_level and int(report[level]) > last_level-4:
                    # print("Safe level")
                    pass
                else: 
                    report_safe = False
                    # print("Unsafe level")
                last_level = int(report[level])
            else:
                last_level = int(report[level])
        
    if report_safe:
        safe_reports += 1

print(safe_reports)