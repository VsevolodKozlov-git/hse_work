

def main(statements, suspects):
    suspect_cnt = count_suspect_feature_match(statements, suspects)
    suspect_ind = index_suspect(suspects)
    best_name, best_cnt = determine_suspect(suspect_cnt, suspect_ind)
    return best_name, best_cnt


def index_suspect(suspects):
    suspect_ind = {}
    for ind, suspect in enumerate(suspects):
        name = suspect['name']
        suspect_ind[name] = ind
    return suspect_ind


def count_suspect_feature_match(statements, suspects):
    suspect_cnt = {}
    for ind, suspect in enumerate(suspects):
        name = suspect['name']
        suspect_cnt[name] = {
            'height': 0,
            'hair': 0,
            'skin': 0,
            'eyes': 0,
            'clothes': 0
        }

    for statement in statements:
        height_min, height_max = statement['height']

        for suspect in suspects:
            name = suspect['name']
            # height processed separately
            if height_min <= suspect['height'] <= height_max:
                suspect_cnt[name]['height'] += 1
            # process other features
            for feature in ['hair', 'skin', 'eyes', 'clothes']:
                if suspect[feature] == statement[feature]:
                    suspect_cnt[name][feature] += 1
    return suspect_cnt


def determine_suspect(suspect_cnt, suspect_ind):
    best_comparison = None
    best_name = None
    best_cnt = None
    for cur_name, features_cnt in suspect_cnt.items():
        cur_min_features = min(features_cnt.values())
        cur_index = suspect_ind[cur_name]
        cur_comparison = (cur_min_features, -cur_index)

        if ((best_comparison is None)
                or
                (cur_comparison > best_comparison)) :
            best_comparison = cur_comparison
            best_name = cur_name
            best_cnt = cur_min_features
    return best_name, best_cnt


#name, cnt = main(statements, suspects)