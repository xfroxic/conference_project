# Frank Goshko 11/11/21
# Conference organizer assignment

import requests
import pprint
from collections import Counter

# dir(requests)
data = requests.get('https://ct-mock-tech-assessment.herokuapp.com/')
# dir(data)
partners = data.json()['partners']

# add more comments

class Partner:
    _all = []

    def __init__(self, dates, country, email, f_name, l_name):
        self.dates = dates
        self.country = country
        self.email = email
        self.f_name = f_name
        self.L_name = l_name
        self._all.append(self)

    def __repr__(self):
        return f'\n <Partner: {self.f_name} {self.L_name} {self.email} {self.country} \n {self.dates}>'


class CalendarManager:
    def __init__(self):
        self.invite_lists = []
        self.invite_list = {}

    def get_partners_by_country(self, country):
        return [x for x in partners if x['country'] == country]

    def get_all_countries(self):
        all_countries = []
        for partner in partners:
            c = partner['country']
            if c not in all_countries:
                all_countries.append(c)
        return all_countries

    # split this into 2 functions (get dates and count dates) for cleaner code
    def get_all_dates(self, partners_by_country):
        all_dates = []
        all_dates_counted = []
        for partner in partners_by_country:
            available_dates = partner['availableDates']
            for available_date in available_dates:
                all_dates.append(available_date)
        all_dates.sort()
        for available_date in all_dates:
            index = self.get_index_for_available_date(all_dates_counted, available_date)
            if index > -1:
                all_dates_counted[index][1] = all_dates_counted[index][1] + 1
            else:
                all_dates_counted.append([available_date, 1])
        return all_dates_counted
        # return all_dates

    def get_index_for_available_date(self, list_of_days, target_day):
        index = 0
        for day in list_of_days:
            if day[0] == target_day:
                return index
            index = index + 1
        return -1

    # Function to add all consecutive days together to find best start date
    def get_two_day_count(self, all_dates_counted):
        two_day_count = {}
        # day_count = all_dates_counted[]
        index = 0
        for date in all_dates_counted:
            day_count = date[1]
            index = index + 1
            if index < len(all_dates_counted):
                day_count += all_dates_counted[index][1]
            two_day_count.update({date[0]: day_count})
        return two_day_count



def main():
    cm = CalendarManager()
    all_countries = cm.get_all_countries()
    partners_canada = cm.get_partners_by_country('Canada')
    dates_canada = cm.get_all_dates(partners_canada)
    abc = cm.get_two_day_count(dates_canada)

    test = ""

main()

# for i in partners:
#     print(i)
#     break

# for i in partners:
#     Partner(
#         dates=i['availableDates'],
#         country=i['country'],
#         email=i['email'],
#         f_name=i['firstName'],
#         l_name=i['lastName']
#     )

# canada = [x for x in partners if x['country'] == 'Canada']
# print (len(canada))
# print (canada)
# locations = sorted(partners, key=lambda p: p['country'])
# print(locations)
# print(Partner._all)

# united_states = [x for x in partners if ['country'] == 'united states']
# print(united_states)

# values_per_key = {}
#
# for d in partners:
#     for k, v in d.items():
#         values_per_key.setdefault(k, set()).add(v)
#
# counts = {k: len(v) for k, v in values_per_key.items()}
# print(counts)

# c = Counter(sum(partners.values(), []))
# # or c = Counter(x for a in d.values() for x in a)
# print(c.most_common())
