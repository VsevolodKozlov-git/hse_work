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

    result = {}
    for name in names:
        avg_seminars = (cnt_grades[name]['Seminar']['sum'] /
                        cnt_grades[name]['Seminar']['cnt'])
        avg_tests = (cnt_grades[name]['Test']['sum'] /
                     cnt_grades[name]['Test']['cnt'])
        result[name] = round(0.7*avg_seminars + 0.3*avg_tests)
    return pd.Series(result)


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

# result = main(grades, excuses, plan)