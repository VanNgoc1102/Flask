import pygsheets

class DataSheet:
    def __init__(self, spreadsheet, working_sheet):
        self.spreadsheet = spreadsheet
        self.working_sheet = working_sheet
        self.gsheet_client = pygsheets.authorize(service_file="/app/src/credentials/credentials.json") 
        self.sheet = None

    def open_work_sheet(self):
        sheet = self.gsheet_client.open(self.spreadsheet)
        worksheet = sheet.worksheet('title', self.working_sheet)   
        return worksheet
    
