#!/usr/bin/env python3
from string import capwords
APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = 'John', job = 'Mason'):
        self.set_name(name)
        self.set_job(job)
    def set_name(self, name):    
        if isinstance(name, str) and 1 <= len(name) <= 25:
             self.name = capwords(name)
        else:
            print('Name must be string between 1 and 25 characters.')    
    def set_job(self, job):        
        if job in APPROVED_JOBS:
            self.job = job
        else:
            print('Job must be in list of approved jobs.')
