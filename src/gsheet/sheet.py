import pygsheets

class DataSheet:

    def open_sheet(spreadsheet, working_sheet):
        gsheet_client = pygsheets.authorize(service_file="src/credentials/credentials.json")    
        sheet = gsheet_client.open(spreadsheet)
        worksheet = sheet.worksheet('title',working_sheet)    
        return(worksheet)