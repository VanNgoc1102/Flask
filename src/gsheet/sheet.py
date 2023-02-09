import pygsheets

class DataSheet:

    def open_sheet(_spreadsheet, _working_sheet):
        gc = pygsheets.authorize(service_file="src/credentials/credentials.json")    
        sh = gc.open(_spreadsheet)
        worksheet = sh.worksheet('title',_working_sheet)    
        return(worksheet)