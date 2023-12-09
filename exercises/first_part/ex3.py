def get_rest_scores(restaurants):
    rest_scores = {}
    point_mapper = {
        '++': 2,
        '+': 1,
        '-': -1,
        '--': -2
    }
    for reviews in restaurants.values():
        for rest, points_str in reviews.items():
            points_int = point_mapper[points_str]
            if rest not in rest_scores:
                rest_scores[rest] = {}
                rest_scores[rest]['min_points'] = 2
                rest_scores[rest]['++'] = 0
            # update minimum points if needed
            if points_int < rest_scores[rest]['min_points']:
                rest_scores[rest]['min_points'] = points_int
            # update ++
            if points_int == 2:
                rest_scores[rest]['++'] += 1
    return rest_scores


def get_best(rest_scores):
    best_restaurant = ''
    rest_best_score = []
    for rest_i, rest_i_score_dict in rest_scores.items():
        rest_i_score = [rest_i_score_dict['min_points'],
                        rest_i_score_dict['++']]
        # init best restaurant if needed
        if best_restaurant == '':
            best_restaurant = rest_i
            rest_best_score = rest_i_score

        if rest_i_score > rest_best_score:
            best_restaurant = rest_i
            rest_best_score = rest_i_score
        # if equal stats, compare by alphabet
        elif rest_i_score == rest_best_score:
            if rest_i < best_restaurant:
                best_restaurant = rest_i
                rest_best_score = rest_i_score

    return best_restaurant


def main(restaurants):
    rest_scores = get_rest_scores(restaurants)
    best_restaurant = get_best(rest_scores)
    return best_restaurant



restaurants = {
    'Alice': {'Pizza Hut': '++', 'Tokyo City': '++', 'Beer House': '+'},
    'Bob': {'Pizza Hut': '+', 'Tokyo City': '+', 'Beer House': '++'},
    'Charlie': {'Pizza Hut': '--', 'Tokyo City': '+', 'Beer House': '++'}
}

best_restaurant = main(restaurants)
# print(best_restaurant)