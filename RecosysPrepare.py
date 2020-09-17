# importing libraries
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


# make cosine similarity matrix and dicts for our recosys recommendations
def data_preparation(dataset, data_type):
    print('Data preparation started.')
    # replacing missing values on unknown
    dataset.fillna('Unknown', inplace=True)

    if data_type == 'anime':
        # make two separate lists to make dict
        id_list = dataset.index.tolist()
        anime_list = dataset.name.tolist()
        # create dicts with id of anime as key and name of anime as value and vice versa
        anime_dict_id = dict(zip(id_list, anime_list))
        anime_dict = dict(zip(anime_list, id_list))

        # create a function to combine the values of important columns into one string
        def get_important_features(data):
            important_features = []
            for i in range(0, data.shape[0]):
                important_features.append(
                    str(data['genre'][i]) + ' ' + str(data['name'][i]))  # +' '+str(data['name'][i]))
            return important_features

        # create a column to hold our features
        dataset['important_features'] = get_important_features(dataset)

        # convert the text into a matrix of token counts
        cm = CountVectorizer().fit_transform(dataset['important_features'])

        # get the cosine similarity matrix from token count matrix
        cs_anime = cosine_similarity(cm)

        print('Data successfully prepared.')
        return cs_anime, anime_dict, anime_dict_id

    elif data_type == 'films':
        # lock our dataset only in usa
        dataset = dataset.loc[(dataset.country == 'USA')]
        # make two separate lists to make dict
        id_list = dataset.index.tolist()
        films_list = dataset.title.tolist()
        # create dicts with id of film as key and name of film as value and vice versa
        films_dict_id = dict(zip(id_list, films_list))
        films_dict = dict(zip(films_list, id_list))

        # create a function to combine the values of important columns into one string
        def get_important_features(data):
            important_features = []
            for i in range(0, data.shape[0]):
                important_features.append(str(data['genre'][i]) + ' ' +
                                          str(data['title'][i]) + ' ' +
                                          str(data['year'][i]) + ' ' +
                                          str(data['director'][i]) + ' ' +
                                          str(data['actors'][i]))
            return important_features

        # create a column to hold our features
        dataset['important_features'] = get_important_features(dataset)

        # convert the text into a matrix of token counts
        cm = CountVectorizer().fit_transform(dataset['important_features'])

        # get the cosine similarity matrix from token count matrix
        cs_films = cosine_similarity(cm)

        print('Data successfully prepared.')
        return cs_films, films_dict, films_dict_id

    elif data_type == 'games':
        # make two separate lists to make dict
        id_list = dataset.index.tolist()
        games_list = dataset.Name.tolist()
        # create dicts with id of game as key and name of game as value and vice versa
        games_dict_id = dict(zip(id_list, games_list))
        games_dict = dict(zip(games_list, id_list))

        # create a function to combine the values of important columns into one string
        def get_important_features(data):
            important_features = []
            for i in range(0, data.shape[0]):
                important_features.append(str(data['Name'][i]) + ' ' +
                                          str(data['Platform'][i]) + ' ' +
                                          str(data['Year_of_Release'][i]) + ' ' +
                                          str(data['Developer'][i]))
            return important_features

        # create a column to hold our features
        dataset['important_features'] = get_important_features(dataset)

        # convert the text into a matrix of token counts
        cm = CountVectorizer().fit_transform(dataset['important_features'])

        # get the cosine similarity matrix from token count matrix
        cs_games = cosine_similarity(cm)

        print('Data successfully prepared.')
        return cs_games, games_dict, games_dict_id
    else:
        # if i forget to set data type:
        print('Choose the type of your recommendation. For example, anime.')
