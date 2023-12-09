import re

def main(actors_and_oscars):
    correct_oscars = {}
    for row in actors_and_oscars:
        name = row[0]
        title = row[1]
        genre_str = list(row[3].keys())[0]
        genres_list = genre_str.split(';')[:2]
        runtime_str = list(row[3].values())[0]
        hours, minutes = re.findall(r'\d+', runtime_str)
        runtime = int(hours) * 60 + int(minutes)

        correct_key = f"[{' and '.join(genres_list)}] {title} with {name}"
        correct_value = runtime
        correct_oscars[correct_key] = correct_value
    return correct_oscars


actors_and_oscars = [['Katharine Hepburn', 'On Golden Pond', 1981, {'Comedy;Drama': '1 hour 49 min'}],
                  ['Julianne Moore', 'Still Alice', 2014, {'Drama': '1:38'}],
                  ['Ingrid Bergman', 'Murder on the Orient Express', 1974, {'Detective;Thriller':'01-49'}],
                  ['Philip Seymour Hoffman', 'Capote', 2005, {'Biography;History;Drama;Crime':'1h 55m'}],
                  ['Jack Nicholson', 'As good as It Gets', 1997, {'Romance;Comedy;History':'2-8'}]]

correct_oscars = main(actors_and_oscars)
# print(correct_oscars)
