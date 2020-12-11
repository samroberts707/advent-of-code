total_yeses = 0
with open ('input.txt', 'r') as _file:
    surveys = _file.read().split('\n\n')
    for survey in surveys:
        survey = survey.split('\n')
        survey_answer_count = len(survey)
        for char in survey[0]:
            letter_count = 0
            for answer in survey:
                if char in answer:
                    letter_count = letter_count + 1
            if letter_count == survey_answer_count:
                total_yeses = total_yeses + 1


print 'Total unique yeses: ' + str(total_yeses)