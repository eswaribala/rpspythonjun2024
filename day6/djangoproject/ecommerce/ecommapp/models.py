from django.db import models
import xml.etree.ElementTree as etree
import json
from abc import ABCMeta, abstractmethod
# Create your models here.

#abstract factory

class VEmployee(metaclass=ABCMeta):
    @abstractmethod
    def payment(self):
        pass

#permanent employee Factory1
class PermanentEmployee(VEmployee):

    def __init__(self,level):
        self.level=level

    def payment(self):
        if self.level==1:
            return HLM()
        if self.level==2:
            return MLM()
        if self.level==3:
            return LLM()


#Contract Employee Factory 2
class ContractEmployee(VEmployee):
    def __init__(self,level):
        self.level=level

    def payment(self):
        if self.level==1:
            return WBC()
        if self.level==2:
            return SBC()

class HLM(models.Model):
    def __init__(self):
        pass


class MLM(models.Model):
    def __init__(self):
        pass

class LLM(models.Model):
    def __init__(self):
        pass


class WBC(models.Model):
    def __init__(self):
        pass

class SBC(models.Model):
    def __init__(self):
        pass


class Employee(models.Model):
    eid = models.CharField(max_length=20,default='0')
    ename = models.CharField(max_length=100,default=' ')
    eemail = models.EmailField(default='sample@gmail.com')
    econtact = models.CharField(max_length=15,default='0000')
    class Meta:
        db_table = "employee"

import logging
#singleton with meta data
class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, \
            cls).__call__(*args, **kwargs)
        return cls._instances[cls]
class Logger(metaclass=MetaSingleton):
    def writeToLog(self,message):
        #self.message=message
        logging.info(message)


#abstract
class FileFactory(metaclass=ABCMeta):
    @staticmethod
    def choose(urlpath):
        if urlpath == 'json':
            return JsonLoader("donut.json")
        if urlpath == 'xml':
            return XmlLoader('person.xml')
    @abstractmethod
    def parsed_data(self):
        pass

#factory pattern
class JsonLoader(FileFactory):

     def __init__(self,filepath):
         with open(filepath, mode='r', encoding='utf-8') as f:
             self.data = json.load(f)

     def parsed_data(self):
         list=[]
         for donut in self.data:
             list.append(donut['name'])
             list.append(donut['ppu'])
         return list


class XmlLoader(FileFactory):
    def __init__(self, filepath):
       self.tree = etree.parse(filepath)

    def parsed_data(self):
        liars = self.tree.findall(".//{}[{}='{}']".format('person',
                                                         'lastName', 'Liar'))
        list=[]
        for liar in liars:
            list.append(liar.find('firstName').text)
            list.append(liar.find('lastName').text)

        return list


