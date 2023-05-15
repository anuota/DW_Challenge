import pandas as pd
import psycopg2
import os
import glob


# connect to postgres database
#parameters
param_dic = {
    "host"      : "localhost",
    "database"  : "postgres",
    "user"      : "postgres",
}

#connect to postgres database
def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn

# execute query

def execute_query(conn, query):
    """ Execute a single query """
    conn = connect(param_dic)
    ret = 0 # Return value
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1

    # If this was a select query, return the result
    if 'select' in query.lower():
        ret = cursor.fetchall()
    cursor.close()
    return ret


# 2nd option create postgres database
def create_postgres (db,new_table):
    cols=cols=','.join([column.replace(" ", "_").replace("?","").lower() + str(' VARCHAR') for column in data.columns.values])

    conn = connect(param_dic)
    cur = conn.cursor()

    #drop table if already exists
    cur.execute("DROP TABLE IF EXISTS %s;"%(new_table))
    #create database
    cur.execute("CREATE TABLE IF NOT EXISTS %s(%s)" %(new_table,(cols))) 
    conn.commit()
    conn.close()

    ## Upload data to the postgres database

def upload_csv_to_postgres(table, csv):
    conn = connect(param_dic)
    cur = conn.cursor()
    try:
        [cur.copy_expert("COPY %s FROM STDIN WITH DELIMITER ',' CSV "%(table), open(csv_file)) for csv_file in files]
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cur.close()
        return 1

    conn.commit()
    conn.close()