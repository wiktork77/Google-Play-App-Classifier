import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
import statistics


def map_probs_with_categories(path):
    with open(path, "r") as file:
        prob_to_cat_dict = {}
        lines = file.readlines()
        for line in lines:
            stripped_line = line.rstrip()
            split = stripped_line.split("\t")
            cat_name = split[0][:-1]
            cat_prob = split[1][:-1]
            cat_prob = cat_prob[:14]
            prob_to_cat_dict[cat_prob] = cat_name
        return prob_to_cat_dict


def extract_score_intervals_with_parameter(df, parameter):
    scores_param_dict = {
        "(4-5]": [],
        "(3-4]": [],
        "(2-3]": [],
        "[1-2]": []
    }
    for row in df.iterrows():
        score = row[1]['score']
        param = row[1][parameter]
        if 5 >= score > 4:
            scores_param_dict['(4-5]'].append(param)
        elif 4 >= score > 3:
            scores_param_dict['(3-4]'].append(param)
        elif 3 >= score > 2:
            scores_param_dict['(2-3]'].append(param)
        elif 2 >= score >= 1:
            scores_param_dict['[1-2]'].append(param)
    mean_dict = {
        "(4-5]": statistics.mean(scores_param_dict["(4-5]"]),
        "(3-4]": statistics.mean(scores_param_dict["(3-4]"]),
        "(2-3]": statistics.mean(scores_param_dict["(2-3]"]),
        "[1-2]": statistics.mean(scores_param_dict["[1-2]"])
    }
    return list(mean_dict.keys()), list(mean_dict.values())


def to_exp_notation(entry_list):
    exp_list = []
    for item in entry_list:
        if len(str(item)) >= 2:
            exponent = math.floor(math.log10(item))
            significand = item // (10 ** exponent)
            if significand != 1:
                formatted_number = "{}*10^{}".format(significand, exponent)
            else:
                formatted_number = "10^{}".format(exponent)
            print(formatted_number)
            exp_list.append(formatted_number)
        else:
            exp_list.append(str(item))
    return exp_list


def visualize_installs(df):
    installs = df['installs']
    installs_dict = {}
    for entry in installs:
        if entry not in installs_dict:
            installs_dict[entry] = 1
        else:
            installs_dict[entry] += 1
    sorted_keys = sorted(installs_dict.keys())
    exp_keys = to_exp_notation(sorted_keys)
    count = []
    for key in sorted_keys:
        count.append(installs_dict[key])

    exp_keys_series = pd.Series(exp_keys)

    sns.barplot(x=exp_keys_series, y=count)
    plt.xticks(fontsize=10)
    for i, tick in enumerate(plt.gca().xaxis.get_major_ticks()):
        if i % 3 != 0:
            tick.set_visible(False)
    plt.xlabel("Number of installs")
    plt.ylabel("Number of apps")
    plt.title("Distribution of the number of applications by download count")
    plt.savefig('./graphs/installs.jpg', format='jpg', dpi=300)
    # plt.show()


def visualize_scores(df):
    scores = df['score']
    sns.kdeplot(data=df, x=scores, fill=True)
    plt.xlabel('App score')
    plt.ylabel('Probability density')
    plt.title('Distribution of the app scores')
    plt.savefig('./graphs/scores.jpg', format='jpg', dpi=300)
    # plt.show()


def visualize_ratings_and_scores(df):
    X, Y = extract_score_intervals_with_parameter(df, 'ratings')
    X.reverse()
    Y.reverse()
    sns.barplot(x=X, y=Y)
    plt.title("Average number of ratings by app belonging to score interval")
    plt.xlabel("Score interval")
    plt.ylabel("Average number of ratings")
    plt.savefig('./graphs/ratings_scores.jpg', format='jpg', dpi=300)
    # plt.show()


def visualize_reviews_and_scores(df):
    X, Y = extract_score_intervals_with_parameter(df, 'reviews')
    X.reverse()
    Y.reverse()
    sns.barplot(x=X, y=Y)
    plt.title("Average number of reviews by app belonging to score interval")
    plt.xlabel("Score interval")
    plt.ylabel("Average number of reviews")
    plt.savefig('./graphs/reviews_scores.jpg', format='jpg', dpi=300)
    # plt.show()


def visualize_categories(df):
    prob_to_cat = map_probs_with_categories("final_categories.txt")
    cats = prob_to_cat.values()
    cat_count = {cat: 0 for cat in cats}
    probs = df['categoryProb']
    for prob in probs:
        cat_count[prob_to_cat[str(prob)[:14]]] += 1
    sorted_dict = dict(sorted(cat_count.items(), key=lambda x: x[1], reverse=True))
    Y = list(sorted_dict.keys())
    X = list(sorted_dict.values())
    print(Y)
    print(X)
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.barplot(x=X, y=Y, orient='h', width=0.75, ax=ax)
    for bars_group in ax.containers:
        ax.bar_label(bars_group, padding=2, fontsize=9)
    ax.set(xlabel="Number of apps", ylabel="Category")

    sns.despine()
    sns.set_style('darkgrid')
    plt.rc('ytick', labelsize=8)
    plt.title("Number of apps from particular categories", fontsize=16)
    plt.tight_layout()
    plt.savefig('./graphs/categories.jpg', format='jpg', dpi=300)
    # plt.show()


def visualize_paid_and_free_apps(df):
    is_free = df['isFree']
    is_free_dict = {
        'free': 0,
        'paid': 0
    }
    for value in is_free:
        if value == 1:
            is_free_dict['free'] += 1
        else:
            is_free_dict['paid'] += 1
    X = ["Free", "Paid"]
    Y = list(is_free_dict.values())
    print(is_free_dict)
    sns.barplot(x=X, y=Y)
    plt.title("Paid and free apps")
    plt.xlabel("App type")
    plt.ylabel("Number of apps")
    plt.savefig('./graphs/paid_free_apps.jpg', format='jpg', dpi=300)
    # plt.show()


data = pd.read_csv("../raw_data/apps_data_complete.csv")
sns.despine()
sns.set_style('darkgrid')
# print(data)

# Należy wykonywać wizualizacje po kolei, tj. 1 na uruchomienie skryptu
# w przeciwnym wypadku wykresy wyglądają inaczej niż powinny


# visualize_installs(data)
# visualize_scores(data)
# visualize_ratings_and_scores(data)
# visualize_reviews_and_scores(data)
# visualize_categories(data)
# visualize_paid_and_free_apps(data)
