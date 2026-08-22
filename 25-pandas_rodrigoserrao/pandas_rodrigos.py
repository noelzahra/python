""" Paddas Rodrigo's module """

import webbrowser

import pandas as pd

df_pokemon = pd.read_csv("pokemon.csv")

def df_summary(df):
    print(f"First 5 rows:\n{df.head()}")
    print(f"List of columns: {list(df.columns)}")
    print(f"Type of DataFrame: {type(df)}")
    print(f"Type of 'english_name' column: {type(df['english_name'])}")
    print(f"Shape of DataFrame: {df.shape}")
    print(f"Length of DataFrame: {len(df['english_name'])}")
    print(f"dtype info:\n{df.dtypes}")

def selected_columns(df) -> pd.DataFrame :
    return df[["hp", "attack", "sp_attack", "sp_defense", "speed"]]

stats = list(selected_columns(df_pokemon).columns)

keep = (["english_name", "gen"] + stats + ["primary_type", "is_sublegendary", "is_legendary", "is_mythical"])
df_chosen_stats = df_pokemon[keep]



def main():
    # df_summary(df_pokemon)
    selected_columns_df = selected_columns(df_pokemon)
    print(selected_columns_df.head(3))
    print(len(df_chosen_stats.columns))
    styled = df_chosen_stats.head(3).style.highlight_max(color="lightgreen")
    styled.to_html("styled_stats.html")
    webbrowser.open("styled_stats.html")

if __name__ == "__main__":
    main()
