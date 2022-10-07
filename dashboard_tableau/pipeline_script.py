#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import getopt
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

if __name__ == '__main__':

    #Задаем входные параметры
    unixOptions = 'sdt:edt:'
    gnuOptions = ['start_dt=', 'end_dt=']
    
    fullCmdArguments = sys.argv
    argumentList = fullCmdArguments[1:] #excluding script name
    
    try:
        arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
    except 
        getopt.error as err:
        print (str(err))
        sys.exit(2)
    
    start_dt = ''
    end_dt = ''
    for currentArgument, currentValue in arguments:
        if currentArgument in ('-sdt', '--start_dt'):
            start_dt = currentValue
        elif currentArgument in ('-edt', '--end_dt'):
            end_dt = currentValue
    
    # Задаём параметры подключения к БД, которые указал админ.
    db_config = {'user': 'prakticum_student',         
                 'pwd': 'Sdf4$2;d-d30pp', 
                 'host': 'rc1b-wcoijxj3yxfsf3fs.mdb.yandexcloud.net',       
                 'port': 6432,              
                 'db': 'data-analyst-zen-project-db'}             
    
    # Формируем строку соединения с БД.
    connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'],
                                                    db_config['pwd'],
                                                    db_config['host'],
                                                    db_config['port'],
                                                    db_config['db'])
    # Подключаемся к БД.
    engine = create_engine(connection_string)
    
    #Теперь выберем из таблицы только те строки,
    #которые были выпущены между start_dt и end_dt
    query = ''' SELECT *, (TIMESTAMP 'epoch' + ts * INTERVAL '1 millisecond') AS dt
            FROM log_raw
            WHERE (TIMESTAMP 'epoch' + ts * INTERVAL '1 millisecond') BETWEEN '{}'::TIMESTAMP AND '{}'::TIMESTAMP
        '''.format(start_dt, end_dt)
    
    log_raw = pd.io.sql.read_sql(query, con = engine)

    # Преобразуем данные к нужному формату.
    log_raw['dt'] = pd.to_datetime(log_raw['dt']).dt.round('T')

    # Готовим агрегирующую таблицу.
    data_dash = (
                log_raw
                .groupby(['item_topic', 'source_topic', 'age_segment', 'dt'])
                .agg({'event': 'count'})
                .reset_index()
    )
    
    #Удаляем старые записи между start_dt и end_dt
    query = '''DELETE FROM data_dash 
               WHERE dt BETWEEN '{}'::TIMESTAMP AND '{}'::TIMESTAMP
            '''.format(start_dt, end_dt)
    engine.execute(query)
    
    # Сохраняем датафрейм в таблицу data_dash базы данных.
    data_dash.to_sql(
        name='data_dash', con=engine, if_exists='append', index=False
    ) 