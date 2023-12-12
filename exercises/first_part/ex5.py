import re

russian_regions = {
    'Moscow': '77',
    'Saint Petersburg': '78',
    'Moscow Oblast': '50',
    'Khanty-Mansi Autonomous Okrug': '86',
    'Yamalo-Nenets Autonomous Okrug': '89',
    'Tatarstan': '16',
    'Krasnodar Krai': '23',
    'Krasnoyarsk Krai': '24',
    'Sverdlovsk Oblast': '66',
    'Samara Oblast': '63',
    'Chelyabinsk Oblast': '74',
    'Rostov Oblast': '61',
    'Bashkortostan': '02',
    'Irkutsk Oblast': '38',
    'Nizhny Novgorod Oblast': '52',
    'Kemerovo Oblast': '42',
    'Perm Krai': '59',
    'Novosibirsk Oblast': '54',
    'Sakha Republic': '14',
    'Tyumen Oblast': '72',
    'Leningrad Oblast': '47',
    'Orenburg Oblast': '56',
    'Belgorod Oblast': '31',
    'Primorsky Krai': '25',
    'Voronezh Oblast': '36',
    'Sakhalin Oblast': '65',
    'Murmansk Oblast': '51',
    'Volgograd Oblast': '34',
    'Stavropol Krai': '26',
    'Vologda Oblast': '35',
    'Saratov Oblast': '64',
    'Khabarovsk Krai': '27',
    'Tula Oblast': '71',
    'Komi Republic': '11',
    'Omsk Oblast': '55',
    'Altai Krai': '22',
    'Lipetsk Oblast': '48',
    'Udmurtia': '18',
    'Dagestan': '05',
    'Vladimir Oblast': '33',
    'Tomsk Oblast': '70',
    'Yaroslavl Oblast': '76',
    'Kursk Oblast': '46',
    'Kaliningrad Oblast': '39',
    'Kaluga Oblast': '40',
    'Astrakhan Oblast': '30',
    'Arkhangelsk Oblast': '29',
    'Tver Oblast': '69',
    'Penza Oblast': '58',
    'Ryazan Oblast': '62',
    'Amur Oblast': '28',
    'Ulyanovsk Oblast': '73',
    'Zabaykalsky Krai': '75',
    'Kirov Oblast': '43',
    'Bryansk Oblast': '32',
    'Karelia': '10',
    'Tambov Oblast': '68',
    'Smolensk Oblast': '67',
    'Nenets Autonomous Okrug': '83',
    'Chuvashia': '21',
    'Buryatia': '03',
    'Novgorod Oblast': '53',
    'Kamchatka Krai': '41',
    'Oryol Oblast': '57',
    'Magadan Oblast': '49',
    'Khakassia': '19',
    'Ivanovo Oblast': '37',
    'Mordovia': '12',
    'Chechnya': '20',
    'Kurgan Oblast': '45',
    'Kostroma Oblast': '44',
    'Mari El': '13',
    'Pskov Oblast': '60',
    'North Ossetia–Alania': '15',
    'Kabardino-Balkaria': '07',
    'Adygea': '01',
    'Chukotka Autonomous Okrug': '87',
    'Karachay-Cherkessia': '09',
    'Kalmykia': '08',
    'Tuva': '17',
    'Jewish Autonomous Oblast': '79',
    'Ingushetia': '06',
    'Altai Republic': '04'
}


def report_refiner(report, *arg_filters, **direction_type):
    """
    interview filters:
        - min_age(int)
        - gender(str)
    market filters:
        - min. proftability(int) (profitability = profit/income)
        - region
    interview:
        - name
        - age
        - gender
        - phone number

    market research:
        - company name
        - url
        - income
        - profit
         - TIN
    return dicts in the same order;
    return empty list if no suitable information
    """
    market_flag = direction_type.get('market', None)
    interview_flag = direction_type.get('interview', None)
    if (market_flag is True) or (interview_flag is False):
        return refine_market(report, *arg_filters)
    elif (interview_flag is True) or (market_flag is False):
        return refine_interview(report, *arg_filters)


def refine_interview(report, *arg_filters):
    # parse filters
    filter_dict = {}
    for filter_value in arg_filters:
        if type(filter_value) == str:
            filter_dict['gender'] = filter_value
        else:
            filter_dict['min_age'] = filter_value
    # parse data
    name_pattern = r"[A-Z][a-z]+ [A-Z][a-z]+"
    names = re.findall(name_pattern, report)

    age_pattern = r"\b(\d+)-year-old\b"
    ages = re.findall(age_pattern, report)
    ages = [int(age) for age in ages]
    gender_pattern = re.compile(r"\bmale\b|\bfemale\b", re.IGNORECASE)
    genders = re.findall(gender_pattern, report)
    phone_pattern = r"\(\d{3}\) \d{3}-\d{4}"
    phone_numbers = re.findall(phone_pattern, report)
    # todo how phone number constructed
    phone_numbers = [
        '+7-' + re.sub(r"\D", "", phone_number)[:3] + '-' + re.sub(r"\D", "", phone_number)[3:6] + '-' + re.sub(
            r"\D", "", phone_number)[6:8] + '-' + re.sub(r"\D", "", phone_number)[8:] for phone_number in
        phone_numbers]

    # Combine all the information into a list of dictionaries
    respondents_info = []
    for ind in range(len(names)):
        name = names[ind]
        age = ages[ind]
        gender = genders[ind].lower()
        phone_number = phone_numbers[ind]

        # todo age < or <= ?
        if ('min_age' in filter_dict) and (age < filter_dict['min_age']):
            continue
        if ('gender' in filter_dict) and (gender != filter_dict['gender']):
            continue
        respondents_info.append({
            'name': name,
            'age': age,
            'gender': gender,
            'phone number': phone_number
        })
    return respondents_info


def refine_market(report, *arg_filters):
    filters_dict = {}
    for filter_value in arg_filters:
        if type(filter_value) == str:
            region = filter_value
            filters_dict['tin'] = int(russian_regions[region])
        else:
            min_profitability = filter_value
            filters_dict['min_profitability'] = min_profitability


    company_pattern = r'(?:[A-Z]\w+\s+){1,}(?:Inc\.|LLC|Ltd\.|Corp\.)'
    url_pattern = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))*\))+(?:\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    income_pattern = r'income of \$(\d{1,3}(?:,\d{3})*)'
    profit_pattern = r'profit of \$(\d{1,3}(?:,\d{3})*)'
    tin_pattern = r'TIN number.+?(\d+)'

    # Find all matches in the report
    companies = remove_duplicates(re.findall(company_pattern, report))
    urls = re.findall(url_pattern, report)
    incomes = [int(income.replace(',', '')) for income in re.findall(income_pattern, report)]
    profits = [int(profit.replace(',', '')) for profit in re.findall(profit_pattern, report)]
    tin_strs = [tin for tin in re.findall(tin_pattern, report)]

    # Combine the results into a list of dictionaries
    results = []
    for i in range(len(companies)):
        company = companies[i].strip()
        url = urls[i]
        tin_str = tin_strs[i]
        income = incomes[i]
        profit = profits[i]
        profitability = profit / income

        if ('min_profitability' in filters_dict and
                profitability < filters_dict['min_profitability']):
            continue
        if ('tin' in filters_dict and
                int(tin_str[:2])!= filters_dict['tin']):
            continue

        results.append({
            'company name': company,
            'url': url,
            'TIN': int(tin_str),
            'income': income,
            'profit': profit
        })

    return results


def remove_duplicates(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]