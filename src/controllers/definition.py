from datetime import datetime, date
import re

class InfoDefinition:
    @staticmethod
    def names(first: str, last: str) -> str:
        return first +' '+ last

    @staticmethod
    def age(born: str) -> int:
        born_date = datetime.strptime(born, "%d/%m/%Y").date()
        today = date.today()
        age = today.year - born_date.year
        # Check if the birthday comes before today in this year
        if (today.month, today.day) < (born_date.month, born_date.day):
            age -= 1
        return age

    @staticmethod
    def check_mail(email: str) -> bool:
        pattern = r'\b[a-zA-Z0-9_.%+-]+@[A-Za-z0-9.-]+\.[a-z|A-Z]{2,4}\b'
        matcher = re.search(pattern, email)
        if matcher:
            return True
        else:
            return False

    @staticmethod
    def process_user(email: str) -> str:
        if InfoDefinition.check_mail(email):
            tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', email)
            return tuples[0][0]
        else:
            return None

    @staticmethod
    def process_vince(adr:str) -> str:
        address = adr.split(",")
        return address[-1].strip()

    @staticmethod
    def process_dis(adr:str) -> str:
        address = adr.split(",")
        if len(address) < 2 :
            return None
        else:
            return address[-2].strip()

