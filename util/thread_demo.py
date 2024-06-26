from time import sleep

import requests
import json
from threading import Thread

response = "Test"


class Source_Code(Thread):

    def __init__(self, url):
        self.response = None
        self.url = url
        # execute the base constructor
        Thread.__init__(self)

    def run(self):
        res = requests.get(self.url)
        sleep(1)
        self.response = json.loads(res.text)


class Build_Thread(Thread):
    def __init__(self, response):
        self.filtered_data = None
        self.response = response
        # execute the base constructor
        Thread.__init__(self)

    def run(self):
        self.filtered_data = []
        for object in self.response:
            # print(object["name"], object["email"], object["address"])
            self.filtered_data.append(str(object["name"]) + "," + str(object["email"]) + "," + str(object["address"]))


class Unit_Test(Thread):
    def __init__(self, filtered_data):
        self.filtered_data = filtered_data
        self.names = None
        # execute the base constructor
        Thread.__init__(self)

    def run(self):
        self.names = []
        for _ in self.filtered_data:
            # print(object)
            namearray = _.split(",")
            self.names.append(namearray[0])


# multi threading
source_code = Source_Code("https://jsonplaceholder.typicode.com/users")
source_code.start()
source_code.join()
# print(source_code.response)
build_thread = Build_Thread(source_code.response)
build_thread.start()
build_thread.join()
unit_test = Unit_Test(build_thread.filtered_data)
unit_test.start()
unit_test.join()
print(unit_test.names)
