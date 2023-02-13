import pandas as pd

from gsheet.sheet import DataSheet
from controllers.definition import InfoDefinition

definition = InfoDefinition()

class YoutubeController:
    def get_data(self):
       self.sheet = DataSheet('Infomation', 'List Data')
       self.worksheet = self.sheet.open_work_sheet()
       info = self.worksheet.get_all_records()
       return(info)

    def process_data(self):
        info = self.get_data()
        df = pd.DataFrame(info)
        lists = ['First_name', 'Last_name', 'Email', 'Born', 'Address']
        drop_first = df.drop_duplicates(lists, keep='first').sort_values(by=lists) 
        drop_last = df.drop_duplicates(lists, keep='last').sort_values(by=lists) 
        inserted = definition.transfo(drop_first,'Timestamp')
        updated = definition.transfo(drop_last,'Timestamp')
        df = drop_first
        name = list(map(definition.names, definition.transfo(df,'First_name'), definition.transfo(df,'Last_name')))
        age = list(map(definition.age_pr, definition.transfo(df,'Born')))
        user_email = list(map(definition.process_user, definition.transfo(df,'Email')))
        province = list(map(definition.process_vince, definition.transfo(df,'Address')))
        district  = list(map(definition.process_dis, definition.transfo(df,'Address')))
        note = list(map(definition.check_mail, definition.transfo(df,'Email')))

        data = {
            'inserted_at': inserted,
            'updated_at': updated,
            'full_name': name,
            'user_email': user_email,
            'age': age,
            'district': district,
            'province': province,
            'note': note
        }
        return(data)

    def write_data_to_db(self):
        data = self.process_data()
        df = pd.DataFrame(data=data)
        self.sheet = DataSheet('Database', 'Data')
        worksheet = self.sheet.open_work_sheet()
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
        




