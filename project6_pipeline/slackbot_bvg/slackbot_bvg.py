import time
import pandas as pd
import requests
from sqlalchemy import create_engine
from sqlalchemy.sql import select

time.sleep(40)
conn_str = 'postgresql://postgres:1234@my_postgres:5432/my_bvg_data'
engine = create_engine(conn_str, echo=True)

query_late='''
    SELECT running_time, delay, type, name, direction
    FROM s_koepenick_timetable
    WHERE delay >60
    ORDER BY running_time DESC
'''

late= pd.read_sql(query_late, engine).drop_duplicates()
text1= "There will be a delay of {delay} seconds on the line {name} from S-Bahn Köpenick at {running_time}.".format(delay=late.at[0, 'delay'], name=late.at[0, 'name'], running_time=late.at[0, 'running_time'] )
text2= "There will be a delay of {delay} seconds on the line {name} from S-Bahn Köpenick at {running_time}.".format(delay=late.at[1, 'delay'], name=late.at[1, 'name'], running_time=late.at[1, 'running_time'] )
text3= "There will be a delay of {delay} seconds on the line {name} from S-Bahn Köpenick at {running_time}.".format(delay=late.at[2, 'delay'], name=late.at[2, 'name'], running_time=late.at[2, 'running_time'] )
WEBHOOK_URL = "https://hooks.slack.com/services/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"
lst = [text1, text2, text3]
text = "\n".join(lst)
json_payload = {'text': text}

requests.post(url=WEBHOOK_URL, json = json_payload)
#query_early = 'SELECT running_time, planned, delay, type, name, direction FROM s_koepenick_timetable WHERE delay =-60 ORDER BY planned LIMIT 3'
#early = pg.execute(query_early)


#print(early)
