#%%
import pandas as pd 
# %%
a_List_Of_Cities = ['Austin', 'New York', 'Toyko', 'Qingdao']


# %%
city_Series = pd.Series(a_List_Of_Cities)
# %%
type(city_Series)
# %%
city_Series.count
# %%
clockWorkOrange = {
    'MovieTitle': 'Clockwork Orange', 'Genre': 'Horror'
}

mandolorian = {
    'MovieTitle': 'The Mandolorian', 'Genre': 'Sci-Fi'
}

pulpFiction = {
    'MovieTitle': 'Pulp Fiction', 'Genre': 'Action'
}
#%%
a_list_of_movies = [clockWorkOrange, mandolorian, pulpFiction]
#%%
movies_df = pd.DataFrame(a_list_of_movies)
# %%
movies_df['MovieTitle']
# %%
