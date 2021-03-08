#Both .loc and .iloc are attributes of dataframes

#%% 
import pandas as pd 
# %%
contacts_path = './contacts.csv'
# %%
contacts_df = pd.read_csv(contacts_path)
# %%
contacts_df
# %%

# %%
def hello(something):
    return print(something)

# %%
newWord = 'hello world'
# %%
hello(newWord)
# %%
