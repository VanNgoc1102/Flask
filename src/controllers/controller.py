import pandas as pd

from gsheet.sheet import DataSheet
from controllers.definition import InfoDefinition

sheet = DataSheet
definition = InfoDefinition

class YoutubeController:
    
    def get_data():
       worksheet = sheet.open_sheet('Infomation', 'List Data')
       info = worksheet.get_all_records()
       return(info)

    def process_data(info):
        df = pd.DataFrame(info)
        lists = ['First_name', 'Last_name', 'Email', 'Born', 'Address']
        drop_first = df.drop_duplicates(lists, keep='first').sort_values(by=lists) 
        drop_last = df.drop_duplicates(lists, keep='last').sort_values(by=lists) 
        inserted = definition.transfo(drop_first,'Timestamp')
        updated= definition.transfo(drop_last,'Timestamp')
        df = drop_first
        name = list(map(definition.names, definition.transfo(df,'First_name'), definition.transfo(df,'Last_name')))
        age = list(map(definition.age_pr, definition.transfo(df,'Born')))
        user_email = list(map(definition.process_user, definition.transfo(df,'Email')))
        provice = list(map(definition.process_vice, definition.transfo(df,'Address')))
        district  = list(map(definition.process_dis, definition.transfo(df,'Address')))
        note = list(map(definition.check_mail, definition.transfo(df,'Email')))

        data = {'inserted_at': inserted,
                'updated_at': updated,
                'full_name': name,
                'user_email': user_email,
                'age': age,
                'district': district,
                'provice': provice,
                'note': note,
                }
        return(data)

    def write_data_to_db(data):
        df = pd.DataFrame(data=data)
        worksheet = sheet.open_sheet('Database', 'Data')
        worksheet.set_dataframe(df,(1,1), escape_formulae=False) 
        return(worksheet)

    def syncdata():    

        info = YoutubeController.get_data()
        data = YoutubeController.process_data(info)
        worksheet = YoutubeController.write_data_to_db(data)
        return(worksheet)




