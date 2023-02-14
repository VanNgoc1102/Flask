import json

import pandas as pd

from gsheet.sheet import DataSheet
from controllers.definition import InfoDefinition

definition = InfoDefinition()

class YoutubeController:
    def get_data(self):
       self.sheet = DataSheet('Infomation', 'List Data')
       worksheet = self.sheet.open_work_sheet()
       info = worksheet.get_all_records()
       return(info)

    def process_data(self):
        info = self.get_data()
        df = pd.DataFrame(info)
        lists = ['First_name', 'Last_name', 'Email', 'Born', 'Address']
        # convert 'Timestamp' sto datetime
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d/%m/%Y %H:%M:%S').dt.strftime('%Y-%m-%d %H:%M:%S')
        # group records by lists the value of 'Insert' and 'Update'
        df_new = df.groupby(lists).agg({'Timestamp': ['min', 'max']})
        df_new.columns = ['inserted_at', 'updated_at']
        df_new = df_new.reset_index()
        # process and add new columns to df_new
        df_new['full_name'] = df_new.apply(lambda row: definition.names(row['First_name'], row['Last_name']), axis=1)
        df_new['user_email'] = df_new.apply(lambda row: definition.process_user(row['Email']), axis=1)
        df_new['age'] = df_new.apply(lambda row: definition.age_pr(row['Born']), axis=1)
        df_new['district'] = df_new.apply(lambda row: definition.process_dis(row['Address']), axis=1)
        df_new['province'] = df_new.apply(lambda row: definition.process_vince(row['Address']), axis=1)
        df_new['note'] = df_new.apply(lambda row: definition.check_mail(row['Email']), axis=1)
        # delete columns  lists = ['First_name', 'Last_name', 'Email', 'Born', 'Address']
        df_new = df_new.drop(columns=lists)
        # convert dataframe df_new to json 
        json_str = df_new.to_json(orient='records',force_ascii=False)
        data = json.loads(json_str)
        return(data)

    def write_data_to_db(self):
        data = self.process_data()
        df = pd.DataFrame(data=data)
        self.sheet = DataSheet('Database', 'Data')
        worksheet = self.sheet.open_work_sheet()
        # Set to googlesheet 
        worksheet.set_dataframe(df,(1,1), escape_formulae=False) 
        return(worksheet)

    def syncdata(self):    
        try:
            self.get_data()
            self.process_data()
            self.write_data_to_db()
        except:
            return ({"message": "sync data failed !"})
        return ({"message": "sync data success !"})
        




