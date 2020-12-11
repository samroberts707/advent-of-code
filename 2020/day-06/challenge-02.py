total_yeses = 0

with open ('input.txt', 'r') as _file:
    surveys = _file.read().split('\n\n')
    for survey in surveys:
        survey = survey.replace('\n', '')
        survey = "".join(set(survey))
        total_yeses = total_yeses + len(survey)

print 'Total unique yeses: ' + str(total_yeses)