from PyPDF2 import PdfReader
from datetime import datetime, timedelta

import requests

class Functions:
    def __init__(self):
        # self.today = datetime.today().date()
        self.today = (datetime.today().date() - timedelta(days=2)).strftime("%Y%m%d")

    def getPDF(self):
        # Get today's date
        today = self.today
        # today = datetime.today().date().strftime("%Y%m%d")
        print(f"Today's date is: {today}")

        url = f"https://www.yzu.edu.tw/admin/ga/files/mail/{today}.pdf"

        re = requests.get(url)
        print(re.status_code)

        if re.status_code == 200:
            with open(f"{today}.pdf", "wb") as file:
                file.write(re.content)
        else:
            print(f"Failed to download PDF. Status code: {re.status_code}")


    def findData(self):
        with open("20240704.pdf", "rb") as file:
            dataList = []
            reader = PdfReader(file)
            n = 0
            for page in reader.pages:
                text = page.extract_text()
                # print(text)
                lines = text.splitlines()
                for line in lines:
                    if line[0] == " ": continue
                    n += 1
                    line = line[len(str(n)):]
                    data = list(map(str, line.split()))
                    if len(data) == 4: data.insert(-1, "")
                    if data[-3] == "教務" :
                        # print(f"{data = }")
                        dataList.append(data)
                
            print(f"{n = }")
            return dataList
