import pandas as pd

def get_data():
    df = pd.read_csv("/Users/laertejt/Projetos/simulados/ex_streamlit/data/athlete_events.csv")
    df_noc = pd.read_csv("/Users/laertejt/Projetos/simulados/ex_streamlit/data/noc_regions.csv")
    df['Age'] = df['Age'].fillna(0) # preenche com 0
    df['Height'] = df['Height'].fillna(0) # preenche com 0
    df['Weight'] = df['Weight'].fillna(0) # preenche com 0
    df['Medal'] = df['Medal'].fillna(0) # preenche com 0
    df.drop_duplicates(inplace=True)
    # Merge
    df = df.merge(df_noc, how='left', on='NOC')
    summer = df.query("Season=='Summer'")
    sorter = ['Gold', 'Silver', 'Bronze']
    grouped = summer.groupby(['NOC'])['Medal'].value_counts().reset_index()
    grouped['Medal'] = grouped.Medal.astype('category').cat.set_categories(sorter)
    top5 = grouped.query("Medal=='Gold'").sort_values('count', ascending=False).head(5)['NOC'].values
    grafico = grouped.query("NOC.isin(@top5)").sort_values(['NOC','Medal','count'], ascending=[False, True, False]).reset_index(drop=True)
    # Grafico do Brasil
    col = ['Name', 'Sex', 'Age', 'Height', 'Weight','Year','Sport', 'Event', 'Medal']
    brazil = summer.query("NOC=='BRA'").loc[~summer.Medal.isna(),col].sort_values(['Year']).reset_index(drop=True)
    grafico2 = brazil.loc[:, ['Year', 'Medal']].groupby(['Year']).count().reset_index()
    # Brazil Single
    brazil_single = brazil.loc[~brazil.Event.str.contains(r'football|Volleyball|basketball', regex=True, case=False),:]
    brazil_single = brazil_single.groupby(['Event'])['Medal'].count().reset_index()
    brazil_single['sport'] = brazil_single.Event.str.split(' ', expand=True).iloc[:,:1]
    grafico3 = brazil_single.drop(['Event'], axis=1).groupby(['sport']).count().sort_values(['Medal'], ascending=False).reset_index()
    dic = {
        "grafico": grafico,
        "grafico2": grafico2,
        "grafico3": grafico3
    }
    return dic

