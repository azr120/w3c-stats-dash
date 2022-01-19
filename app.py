import dash
import dash_table
import pandas as pd


#test
df = pd.read_csv('https://raw.githubusercontent.com/azr120/w3c-stats-dash/master/dash-profiles.csv?token=GHSAT0AAAAAABJ5EIVY5EEOI5NNGKZTFFKUYPH7UQA')


app = dash.Dash(__name__)

# Index(['battleTag', 'race', 'raceId', 'Games', 'HeroScorePM', 'UnitScorePM',
#        'GPM', 'LPM', 'UpkeepPM', 'ResourceScorePM', 'TotalScorePM',
#        'Unit-res-ratio', 'Gold-Lumber-Ratio', 'Duration', 'TotalVs', 'HeroVs',
#        'GoldVs', 'UnitVs', 'Kill-Participation', 'Hero_combo', 'No. heroes',
#        'HeroKills', 'opponentHeroKills', 'Tech Pct', 'Mercs', 'Items',
#        'Largest Army', 'MMR', 'League', 'opponentMMR', 'Playtime', 'Won',
#        'Lost', 'Winrate', 'Exp. Winrate', 'Ping'],
#       dtype='object')

app.layout = dash_table.DataTable(
    columns=[
        {'name': 'battleTag', 'id': 'battleTag', 'type': 'text'},
        {'name': 'race', 'id': 'race', 'type': 'text'},
        {'name': 'raceId', 'id': 'raceId', 'type': 'text'},
        {'name': 'Games', 'id': 'Games', 'type': 'numeric'},
        {'name': 'HeroScorePM', 'id': 'HeroScorePM', 'type': 'numeric'},
        {'name': 'UnitScorePM', 'id': 'UnitScorePM', 'type': 'numeric'},
        {'name': 'GPM', 'id': 'GPM', 'type': 'numeric'},
        {'name': 'LPM', 'id': 'LPM', 'type': 'numeric'},
        {'name': 'UpkeepPM', 'id': 'UpkeepPM', 'type': 'numeric'},
        {'name': 'ResourceScorePM', 'id': 'ResourceScorePM', 'type': 'numeric'},
        {'name': 'TotalScorePM', 'id': 'TotalScorePM', 'type': 'numeric'},
        {'name': 'Unit-res-ratio', 'id': 'Unit-res-ratio', 'type': 'numeric'},
        {'name': 'Gold-Lumber-Ratio', 'id': 'Gold-Lumber-Ratio', 'type': 'numeric'},
        {'name': 'Duration', 'id': 'Duration', 'type': 'numeric'},
        {'name': 'TotalVs', 'id': 'TotalVs', 'type': 'numeric'},
        {'name': 'HeroVs', 'id': 'HeroVs', 'type': 'numeric'},
        {'name': 'GoldVs', 'id': 'GoldVs', 'type': 'numeric'},
        {'name': 'UnitVs', 'id': 'UnitVs', 'type': 'numeric'},
        {'name': 'Kill-Participation', 'id': 'Kill-Participation', 'type': 'numeric'},
        {'name': 'Hero_combo', 'id': 'Hero_combo', 'type': 'text'},
        {'name': 'No. heroes', 'id': 'No. heroes', 'type': 'numeric'},
        {'name': 'HeroKills', 'id': 'HeroKills', 'type': 'numeric'},
        {'name': 'opponentHeroKills', 'id': 'opponentHeroKills', 'type': 'numeric'},
        {'name': 'Tech Pct', 'id': 'Tech Pct', 'type': 'numeric'},
        {'name': 'Mercs', 'id': 'Mercs', 'type': 'numeric'},
        {'name': 'Items', 'id': 'Items', 'type': 'numeric'},
        {'name': 'Largest Army', 'id': 'Largest Army', 'type': 'numeric'},
        {'name': 'MMR', 'id': 'MMR', 'type': 'numeric'},
        {'name': 'League', 'id': 'League', 'type': 'numeric'},
        {'name': 'opponentMMR', 'id': 'opponentMMR', 'type': 'numeric'},
        {'name': 'Playtime', 'id': 'Playtime', 'type': 'numeric'},
        {'name': 'Won', 'id': 'Won', 'type': 'numeric'},
        {'name': 'Lost', 'id': 'Lost', 'type': 'numeric'},
        {'name': 'Winrate', 'id': 'Winrate', 'type': 'numeric'},
        {'name': 'Exp. Winrate', 'id': 'Exp. Winrate', 'type': 'numeric'},
        {'name': 'Ping', 'id': 'Ping', 'type': 'numeric'}
    ],
    data=df.to_dict('records'),
    filter_action='native',

    style_table={
        'height': 400,
    },
    style_data={
        'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)