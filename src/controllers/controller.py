import json

import pandas as pd

from gsheet.sheet import DataSheet
from controllers.definition import InfoDefinition

definition = InfoDefinition()

class YoutubeController:
    def get_data(self):
        # access DataSheet object with name "Information" and sheet name "List Data"
        self.sheet = DataSheet('Infomation', 'List Data')
        worksheet = self.sheet.open_work_sheet()
        # get all records from googlesheet 
        info = worksheet.get_all_records()
        return(info)

    def process_data(self):
        info = self.get_data()
        df = pd.DataFrame(info)
        lists = ['full_name', 'user_email', 'age', 'district', 'provice']
        time = df.get('Timestamp').tolist()
        full_name = df.apply(definition.full_name, axis=1).tolist()
        user_email = df.apply(definition.process_user, axis=1).tolist()
        age = df.apply(definition.age_pr, axis=1).tolist()
        district = df.apply(definition.process_dis, axis=1).tolist()
        provice = df.apply(definition.process_vince, axis=1).tolist()
        note = df.apply(definition.check_mail, axis=1).tolist()
        data = {
                'time': time,
                'full_name': full_name,
                'user_email': user_email,
                'age': age,
                'district': district,
                'provice': provice,
                'note': note,
                }
        dff = pd.DataFrame(data)
        merged_df = pd.merge(dff.drop_duplicates(subset=lists, keep='first'), dff.drop_duplicates(subset=lists, keep='last'),on=lists,how='outer',suffixes=['_inserted', '_updated'])
        json_data = merged_df.to_dict('list')
        return(json_data)

    def write_data_to_db(self):
        data = self.process_data()
        df = pd.DataFrame(data=data)
        # access new DataSheet object with name "Database" and sheet name "Data"
        self.sheet = DataSheet('Database', 'Data')
        worksheet = self.sheet.open_work_sheet()
        # set data to googlesheet 
        worksheet.set_dataframe(df,(1,1), escape_formulae=False) 
        return(worksheet)

    def syncdata(self):    
        self.get_data()
        self.process_data()
        self.write_data_to_db()
        
        




