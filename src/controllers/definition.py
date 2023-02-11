from datetime import datetime, date
import re

class InfoDefinition:

    def names(first: str, last: str):
        return first +' '+ last

    def process_name(first:list, last:list):
        name = list(map(names, first, last))
        return name

    def age_pr(born):
        born = datetime.strptime(born, "%d/%m/%Y").date()
        today = date.today()
        return today.year - born.year - ((today.month, 
                                        today.day) < (born.month, 
                                                        born.day))

    def check_mail(email):
        pattern = r'\b[a-zA-Z0-9_.%+-]+@[A-Za-z0-9.-]+\.[a-z|A-Z]{2,4}\b'
        ''' \	Signals a special sequence (can also be used to escape special characters)
            \b	Returns a match where the specified characters are at the beginning or at the end of a word
               (the "r" in the beginning is making sure that the string is being treated as a "raw string")'''
        matcher = re.search(pattern, email)
        if matcher:
            return True
        else:
            return False


    def process_user(email):
        mail = InfoDefinition
        if mail.check_mail(email):
            tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', email)
            return(tuples[0][0])
        else:
            return None

    def process_vince(adr:str):
        address = adr.split(",")
        return(address[-1])

    def process_dis(adr:str):
        address = adr.split(",")
        if len(address) < 2 :
            return None
        else:
            return(address[-2])

    def transfo(df, name: str):
        return df.get(name).to_list()        
