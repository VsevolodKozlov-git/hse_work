import re

def money_to_int(s):
    return float(s[1:-1])

def main(olympic_games):

    mid_results = {}

    for key, exp_rev_dict in olympic_games.items():
        pattern = r'^((?:\w+\b\s*)+)\((\w+)\)\s+(\d+)'
        city, country_code, year = re.findall(pattern, key)[0]
        expenses = money_to_int(exp_rev_dict['expenses'])
        revenue = money_to_int(exp_rev_dict['revenue'])

        if country_code not in mid_results:
            mid_results[country_code] = {'info': [], 'value': 0}
        mid_results[country_code]['info'].append(f'{city} {year}')
        mid_results[country_code]['value'] += round(revenue - expenses, 2)


    fin_results = {}
    for country_code in mid_results:
        fin_results[country_code] = {}
        fin_results[country_code]['info'] = sorted(mid_results[country_code]['info'])
        value = mid_results[country_code]['value']
        if value < 0:
            fin_results[country_code]['loss'] = -value
        else:
            fin_results[country_code]['profit'] = value

    return fin_results


#fin_results = main(olympic_games)


