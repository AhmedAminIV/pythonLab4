import json
import requests


class Queue:
    def __init__(self):
        self.queue = list()

    def insert(self, value):
        self.queue.append(value)

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def pop(self):
        if not self.is_empty():
            front = self.queue[0]
            del self.queue[0]
            print(self.queue)
            return front
        else:
            print(f"Warning: Empty Queue!!")
            return None


# q1 = Queue()
# q1.insert(5)
# q1.insert(6)
# q1.insert(7)
#
#
# print(q1.pop())


class EnhancedQ(Queue):
    created_q = list()

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = self.set_size(size)
        self.dict = {'name': self.name, 'queue_items': self.queue}
        self.created_q.append(self.dict)

    def set_size(self, sz):
        if isinstance(sz, int):
            return sz
        else:
            raise Exception('SizeMustBeInt')

    def is_full(self):
        if len(self.queue) == self.size:
            return True
        else:
            return False

    def insert(self, value):
        if not self.is_full():
            self.queue.append(value)
        else:
            raise Exception("QueueOutOfRangeException")

    @classmethod
    def load(cls):
        try:
            with open('data.json', 'r') as file_object:
                data = file_object.read()
                dict_data = json.loads(data)
                print(dict_data)
                cls.created_q = dict_data

        except Exception as e:
            print(e)

    @classmethod
    def save(cls):
        try:
            with open('data.json', 'w') as file_object:
                all_q_data = cls.created_q
                data = json.dumps(all_q_data, indent=4)  # convert list of dicts to string
                file_object.write(data)  # write data to the file
        except Exception as e:
            print(e)


#
# eq1 = EnhancedQ('first', 5)
# eq1.insert(5)
# eq1.insert(6)
# eq1.insert('ahmed')
#
# eq2 = EnhancedQ('second', 10)
# eq2.insert(7)
# eq2.insert(7)
# eq2.insert(7)
# eq2.insert(7)
#
# EnhancedQ.save()
# EnhancedQ.load()


class WeatherApi:
    def __init__(self):
        self.key = 'cdbede36882e46fc899172223232208'
        self.url = 'http://api.weatherapi.com/v1/'

    def get_current_temperature(self, city):
        response = requests.get(f"{self.url}current.json?key={self.key}&q={city}&aqi=yes")
        temp_dict = (response.json())
        country = temp_dict['location']['country']
        name = temp_dict['location']['name']
        region = temp_dict['location']['region']
        time = temp_dict['current']['last_updated']
        temp_c = temp_dict['current']['temp_c']
        temp_f = temp_dict['current']['temp_f']
        print(f"\nCountry: {country}\nRegion: {region}\nArea: {name}\nTime: {time}\ntemp_c: {temp_c}\ntemp_f: {temp_f}")

    def get_temperature_after(self, city, days, hours=None):
        if isinstance(days, int) and 1 <= days <= 10:
            response = requests.get(f"{self.url}forecast.json?key={self.key}&q={city}&days={days}&aqi=no&alerts=no")
            temp_dict = (response.json())
            country = temp_dict['location']['country']
            name = temp_dict['location']['name']
            region = temp_dict['location']['region']

            for day in temp_dict['forecast']['forecastday']:
                date = day['date']
                max_temp_c = day['day']['maxtemp_c']
                min_temp_c = day['day']['mintemp_c']
                avg_temp_c = day['day']['avgtemp_c']
                print(f"\nCountry: {country}\nRegion: {region}\nArea: {name}\nDate: {date}\nmax_temp_c: "
                      f"{max_temp_c}\nmin_temp_: {min_temp_c}\navg_temp_c: {avg_temp_c}")
                if hours:
                    for hour in day['hour']:
                        time = hour['time']
                        temp_c = hour['temp_c']
                        print(f"\nTime: {time}\t\ttemp_c: {temp_c}")
        else:
            raise Exception("days Must be integer and between 1 and 10")

    def get_lat_and_long(self, city):
        response = requests.get(f"{self.url}current.json?key={self.key}&q={city}&aqi=yes")
        temp_dict = (response.json())
        country = temp_dict['location']['country']
        name = temp_dict['location']['name']
        region = temp_dict['location']['region']
        lat = temp_dict['location']['lat']
        lon = temp_dict['location']['lon']
        print(f"\nCountry: {country}\nRegion: {region}\nArea: {name}\nLatitude: {lat}\nLongitude: {lon}")
# new = WeatherApi()
# new.get_current_temperature('Egypt')
#
# asd = WeatherApi()
# asd.get_temperature_after('Cairo', 1, True)
#
# lst = WeatherApi()
# lst.get_lat_and_long('Nasr City')
