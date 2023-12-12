import pandas as pd
from datetime import datetime

def main(grades, excuses, plan):
    # prepare dataframes
    grades = grades.T
    plan.set_index('date', inplace=True)
    plan = plan.to_dict()['activity']

    excuses[['start_date', 'end_date']] = excuses['date'].str.split(expand=True)
    excuses['start_date'] = pd.to_datetime(excuses['start_date'])
    excuses['end_date'] = pd.to_datetime(excuses['end_date'])
    excuses.drop('date', axis=1, inplace=True)

    cnt_grades = count_grades(grades, excuses, plan)
    return get_result(cnt_grades)


def prepare_excuses(excuses):
    excuses[['start_date', 'end_date']] = excuses['date'].str.split(expand=True)
    excuses['start_date'] = pd.to_datetime(excuses['start_date'])
    excuses['end_date'] = pd.to_datetime(excuses['end_date'])
    excuses.drop('date', axis=1, inplace=True)
    return excuses

def count_grades(grades, excuses, plan):
    cnt_grades = {}
    names = grades.columns
    for name in names:
        cnt_grades[name] = {'Seminar': {'sum': 0, 'cnt': 0},
                            'Test': {'sum': 0, 'cnt': 0}}
    for date, row in grades.iterrows():
        activity = plan[date]
        for name in names:
            value = row[name]
            if pd.isna(value):
                is_valid = is_valid_excuse(excuses, date, name)
                if is_valid:
                    continue
                else:
                    cnt_grades[name][activity]['cnt'] += 1
            else:
                cnt_grades[name][activity]['cnt'] += 1
                cnt_grades[name][activity]['sum'] += value
    return cnt_grades

def is_valid_excuse(excuses, date, name):
    date = datetime.strptime(date, "%Y-%m-%d")
    filtered_df = excuses[(excuses['start_date'] <= date) & (excuses['end_date'] >= date)]
    filtered_df = filtered_df[filtered_df['name'] == name]
    if len(filtered_df) == 0:
        return False
    else:
        reason = filtered_df.iloc[0]['reason']
        if reason == 'valid':
            return True
        return False


def get_result(cnt_grades):
    result = {}
    for name in cnt_grades:
        if cnt_grades[name]['Seminar']['cnt'] != 0:
            avg_seminars = (cnt_grades[name]['Seminar']['sum'] /
                            cnt_grades[name]['Seminar']['cnt'])
        else:
            avg_seminars = 0

        if cnt_grades[name]['Test']['cnt'] != 0 :
            avg_tests = (cnt_grades[name]['Test']['sum'] /
                         cnt_grades[name]['Test']['cnt'])
        else:
            avg_tests = 0
        result[name] = round(0.7*avg_seminars + 0.3*avg_tests)
    return pd.Series(result)



#result = main(grades, excuses, plan)