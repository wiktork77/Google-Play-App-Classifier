import pandas as pd
import statistics


def provide_statistics(title, data):
    print("="*25, end="")
    print(title, end="")
    print("="*25)
    print(f"min: {min(data)}")
    print(f"max: {max(data)}")
    mean = statistics.mean(data)
    print(f"mean: {mean}")
    print(f"stdev: {statistics.stdev(data, xbar=mean)}")
    num = 50 + len(title)
    print("="*num)
    print()


def check_scores(data):
    scores = data['score']
    scores_dict = {}
    for score in scores:
        if score not in scores_dict:
            scores_dict[score] = 1
        else:
            scores_dict[score] += 1
    return scores_dict


data = pd.read_csv("../raw_data/apps_data_complete.csv")

installs = data['installs']
scores = data['score']
ratings = data['ratings']
reviews = data['reviews']
is_free = data['isFree']

provide_statistics("installs", installs)
provide_statistics("score", scores)
provide_statistics("ratings", ratings)
provide_statistics("reviews", reviews)
provide_statistics("is_free", is_free)

# scores_data = check_scores(data)
# sorted_dict = dict(sorted(scores_data.items(), key=lambda x: x[1], reverse=True))
# print(sorted_dict)