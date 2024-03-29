from datetime import datetime, date
import re

class InfoDefinition:
    @staticmethod
    def full_name(row):
        return row.get('First_name') +' '+ row.get('Last_name')

    @staticmethod
    def age_pr(born):
        born_date = datetime.strptime(born.get('Born'), "%m/%d/%Y").date()
        today = date.today()
        age = today.year - born_date.year
        # Check if the birthday comes before today in this year
        if (today.month, today.day) < (born_date.month, born_date.day):
            age -= 1
        return age

    @staticmethod
    def check_mail(email):
        pattern = r'\b[a-zA-Z0-9_.%+-]+@[A-Za-z0-9.-]+\.[a-z|A-Z]{2,4}\b'
        matcher = re.search(pattern, email.get('Email Address'))
        if matcher:
            return True
        else:
            return False

    @staticmethod
    def process_user(email):
        if InfoDefinition.check_mail(email):
            tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', email.get('Email Address'))
            return tuples[0][0]
        else:
            return None

    @staticmethod
    def process_vince(adr):
        address = adr.get('Address').split(",")
        return address[-1].strip()

    @staticmethod
    def process_dis(adr):
        address = adr.get('Address').split(",")
        if len(address) < 2 :
            return None
        else:
            return address[-2].strip()

