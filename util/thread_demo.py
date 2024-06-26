import requests
import json
import threading

response = "Test"
def source_code():
    global response
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    response = json.loads(res.text)
    print(response)


# def build(data):
#     filtered_data = []
#     for object in data:
#         # print(object["name"], object["email"], object["address"])
#         filtered_data.append(str(object["name"]) + "," + str(object["email"]) + "," + str(object["address"]))
#
#
# def unit_test(filtered_data):
#     names = []
#     # print(filtered_data)
#     for _ in filtered_data:
#         # print (_,end="\n")
#         namearray = _.split(",")
#         names.append(namearray[0])


thread1 = threading.Thread(name="source_code", target=source_code)
thread1.start()

