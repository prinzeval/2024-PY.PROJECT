from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:Vondabaic2020@localhost/val_data")

def load_data_from_db(table_name):
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM {table_name}"))
        column_result = result.keys()
        dict_result = [dict(zip(column_result, row)) for row in result.fetchall()]
        return dict_result
movies = load_data_from_db("Movies")
episodes = load_data_from_db("Episodes")
