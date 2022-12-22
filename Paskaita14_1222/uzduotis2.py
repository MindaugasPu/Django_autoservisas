# Iš šio teksto atspausdinkite datų sąrašą.

import re

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

def datos(tekstas):
    pattern = re.compile(r'\w+\s\d{2},\s\d{4}$', re.M)
    rezultatas = pattern.findall(tekstas)
    print(rezultatas)

datos(text)
