# importing libraries
import pandas as pd
# importing modules
import RecosysPrepare
import RecosysAuthorization

# get our datasets
anime_data = pd.read_csv('./anime_dataset/anime.csv')
films_data = pd.read_csv('./films_dataset/IMDb movies.csv')
games_data = pd.read_csv('./games_dataset/Video_Games_Sales_as_at_22_Dec_2016.csv')


def get_recommendation(name, dataset_type, recotype='normal'):
    """
    This function make recommendations based on items.

    :type dataset_type: str
    :param name: used for make recommendations (item-based filtering)
    :param dataset_type: type of data used in recommendations
    :param recotype: type of recommendations (normal or vk-type)
    :return: none
    """
    print('Initializing of recosys.')
    global cs, name_dict, name_dict_id
    if dataset_type == 'anime':
        cs, name_dict, name_dict_id = RecosysPrepare.data_preparation(anime_data, 'anime')
    elif dataset_type == 'films':
        cs, name_dict, name_dict_id = RecosysPrepare.data_preparation(films_data, 'films')
    elif dataset_type == 'games':
        cs, name_dict, name_dict_id = RecosysPrepare.data_preparation(games_data, 'games')
    else:
        print('Choose the dataset type.')

    # get id of name
    name_id = name_dict[name]

    # find a list of enumerations for the similarity score [ (name_id, similarity score), (...) ]
    scores = list(enumerate(cs[name_id]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    sorted_scores = sorted_scores[1:]

    if recotype == 'normal':
        # create a loop to print the first 7 similar items
        j = 0
        print('The 7 most recommended to', name, 'are:\n')
        for item in sorted_scores:
            title = name_dict_id[item[0]]
            names_sim_rate = round(item[1], 2) * 100
            print(j + 1, '-', title, ' ', 'Similarity rate:', names_sim_rate, '%')
            j += 1
            if j > 6:
                break
    else:
        print('Write something to get ID.')
        this_user_id = RecosysAuthorization.get_user_id()
        print('User ID:', this_user_id)
        j = 0
        RecosysAuthorization.vk.messages.send(user_id=this_user_id, random_id=RecosysAuthorization.random,
                                              message='Топ 7 для просмотра/прохождения, основываясь на введённом:')
        RecosysAuthorization.random += 1
        # create a loop to print the first 7 similar items
        for item in sorted_scores:
            title = name_dict_id[item[0]]
            RecosysAuthorization.vk.messages.send(user_id=this_user_id, random_id=RecosysAuthorization.random,
                                                  message=str(j+1) + ' - ' + title)
            RecosysAuthorization.random += 1
            j += 1
            if j > 6:
                break
