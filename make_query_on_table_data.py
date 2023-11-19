import pandas as pd
import sqlite3
from sqlalchemy import create_engine
import openai
import os

openai.api_key = "Provide your API key here"


def read_details_from_file(file_path, table_name):
    df = pd.read_csv(file_path)
    df.columns = [col.replace(" ", "_").lower() for col in df.columns]
    all_columns = df.columns.tolist()
    return df, all_columns, table_name


def save_as_db(data_frame, save_db_name, table_name):
    if not os.path.exists(save_db_name):
        print("creating DB File")
        engine = create_engine(f'sqlite:///{save_db_name}', echo=False)
        data_frame.to_sql(table_name, con=engine, if_exists='replace', index=False)
    return 0


def create_connection_and_pass_query(save_db_name, query):
    con = sqlite3.connect(save_db_name)
    data = pd.read_sql_query(query, con)
    return data


def generate_sql(table_naming, col_lst, question):
    model_engine = "text-davinci-003"
    prompt = (
        f"Write a SQL Query given the table name {table_naming} and columns as a list {col_lst} for the given "
        f"question : {question}.")
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["#", ";"]
    )
    return response.choices[0].text.strip()


def console_ops(file_location_path, query):
    split_by_slash = file_location_path.split("/")
    db_name = "/".join(split_by_slash[0:-1]) + "/" + split_by_slash[-1].split(".")[0] + ".db"
    name_table = "temp_table"
    df, all_columns, table_name = read_details_from_file(file_location_path, name_table)
    save_as_db(df, db_name, name_table)
    generated_query = generate_sql(table_name, all_columns, query)
    res = create_connection_and_pass_query(db_name, generated_query)
    return res


if __name__ == "__main__":
    data_path = ""
    query_question = ""
