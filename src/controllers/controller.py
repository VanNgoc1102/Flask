import json

import pandas as pd

from gsheet.sheet import DataSheet
from controllers.definition import InfoDefinition

definition = InfoDefinition()

class YoutubeController:
    def get_data(self):
        # access DataSheet object with name "Information" and sheet name "List Data"
        self.sheet = DataSheet('Information', 'List Data')
        worksheet = self.sheet.open_work_sheet()
        # get all records from googlesheet 
        info = worksheet.get_all_records()
        return(info)

    def process_data(self):
        info = self.get_data()
        df_info = pd.DataFrame(info)
        df_info['Timestamp'] = pd.to_datetime(df_info['Timestamp'], format='%m/%d/%Y %H:%M:%S')
        df_info = df_info.rename(columns={'Timestamp': 'create_at'})
        df_info.insert(1, 'update_at', df_info['create_at'].copy())

        self.sheet = DataSheet('Database', 'Data')
        worksheet = self.sheet.open_work_sheet()
        record = worksheet.get_all_records()
        df_record = pd.DataFrame(record)

        if df_record.empty:
            df_record = df_info.head(1)
        else:
            time_df = df_record['update_at'].iloc[-1]  
            df_new = df_info[df_info['create_at'] > time_df]
                
            for index1, value1 in df_new["Email Address"].iteritems():
                if value1 in df_record["Email Address"].values:
                    index2 = df_record.index[df_record['Email Address'] == value1].tolist()
                    df_record.loc[index2, 'update_at'] = df_new.loc[index1, 'create_at']
                else:
                    new_row = df_new.loc[index1]
                    df_record = df_record.append(new_row, ignore_index=True)

        data = df_record.to_dict('list')
        return(data)

    def write_data_to_db(self):
        data = self.process_data()
        df = pd.DataFrame(data=data)
        
        create_at = df.get('create_at').tolist()
        update_at = df.get('update_at').tolist()
        full_name = df.apply(definition.full_name, axis=1).tolist()
        user_email = df.apply(definition.process_user, axis=1).tolist()
        age = df.apply(definition.age_pr, axis=1).tolist()
        district = df.apply(definition.process_dis, axis=1).tolist()
        provice = df.apply(definition.process_vince, axis=1).tolist()
        note = df.apply(definition.check_mail, axis=1).tolist()
        db = {
                'create_at': create_at,
                'update_at': update_at,
                'full_name': full_name,
                'user_email': user_email,
                'age': age,
                'district': district,                                                                   
                'provice': provice,
                'note': note,
                }
        dff = pd.DataFrame(db)
        
        self.sheet = DataSheet('Database', 'DB')
        worksheet = self.sheet.open_work_sheet()
        # set data to googlesheet 
        worksheet.set_dataframe(dff,(1,1), escape_formulae=False) 
        return(worksheet)

    def syncdata(self):    
        try:
            self.get_data()
            self.process_data()
            self.write_data_to_db()
            return ({"message": "sync data success !"})
        except:
            return ({"message": "sync data failed !"})
            
        
        




