import json

import requests


def source_code(next_coroutine=None):
    try:
        while True:
            url = (yield)
            res = requests.get(url)
            response = json.loads(res.text)
            #print(response)
            next_coroutine.send(response)
    except GeneratorExit:
        print("Done with Source Code Fetching!!")
        next_coroutine.close()


def build(next_coroutine):
    filtered_data = []
    try:
        while True:
            response = (yield)
            for object in response:
               # print(object["name"], object["email"], object["address"])
                filtered_data.append(str(object["name"])+","+str(object["email"])+","+str(object["address"]))
            next_coroutine.send(filtered_data)
    except GeneratorExit:
        print("Done with Build!!")
        next_coroutine.close()


def unit_test(next_coroutine):
    try:
        while True:
            filtered_data = (yield)
            next_coroutine.send(filtered_data)
    except GeneratorExit:
        print("Done with Unit Testing!!")
        next_coroutine.close()


def integrate(next_coroutine):
    try:
        while True:
            url = (yield)
            next_coroutine.send(url)
    except GeneratorExit:
        print("Done with Integration!!")
        next_coroutine.close()


def e2e_test(next_coroutine):
    try:
        while True:
            url = (yield)
            next_coroutine.send(url)
    except GeneratorExit:
        print("Done with E2E Testing!!")
        next_coroutine.close()


def deployment():
    try:
        while True:
            url = (yield)
            print(url)
    except GeneratorExit:
        print("Done with Deployment!!")


def trigger_pipeline(url, next_coroutine):
    next_coroutine.send(url)
    next_coroutine.close()


# coroutine pipeline
pipeline = deployment()
pipeline.__next__()
pipeline = e2e_test(next_coroutine=pipeline)
pipeline.__next__()
pipeline = integrate(next_coroutine=pipeline)
pipeline.__next__()
pipeline = unit_test(next_coroutine=pipeline)
pipeline.__next__()
pipeline = build(next_coroutine=pipeline)
pipeline.__next__()
pipeline = source_code(next_coroutine=pipeline)
pipeline.__next__()

url = input("Enter Source code url")
trigger_pipeline(url, pipeline)
