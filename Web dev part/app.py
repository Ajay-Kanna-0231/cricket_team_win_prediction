from flask import Flask, request, render_template
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.orm import sessionmaker
import pickle

app = Flask(__name__)

# Database setup
DATABASE_URI = 'postgresql://postgres:Parrot%40123@localhost:5432/postgres'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/find-players', methods=['GET', 'POST'])
def find_players():
    player_data = {}
    if request.method == 'POST':
        name = request.form['name']
        stats_type = request.form['stats_type']
        inspector = inspect(engine)
        column_names = [col['name'] for col in inspector.get_columns('cricket_data', schema='public')]
        if stats_type != 'all':
           filtered_column_names = ['name', 'country', 'Full name', 'born', 'died', 'Current age', 'Major teams', 'education', 'height', 'nickname', 'Playing role', 'Batting style', 'Bowling style', 'description']
           filtered_column_names += [col for col in column_names if stats_type.lower() in col.lower()]
        else:
            filtered_column_names = [col for col in column_names if col not in ["id", "other", "relation", "In a nutshell"]]

        # Fetch player stats from the database using text()
        quoted_columns = [f'"{col}"' for col in filtered_column_names]
        query_columns = ', '.join(quoted_columns)
        query = text(f"SELECT {query_columns} FROM public.cricket_data WHERE name = :name")

        result = session.execute(query, {'name': name}).fetchone()
        if result:
            # convert the result of values into a dict with keys as stats and values as values
            player_data = dict(zip(filtered_column_names, result))
            return render_template('results.html', player_data=player_data)
        else:
            return render_template('find_players.html', error="Player not found")
    return render_template('find_players.html')

@app.route('/go-back')
def go_back():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
