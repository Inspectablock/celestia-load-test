from locust import HttpUser, task, between, events
from locust.runners import MasterRunner
import requests
import json

class QuickstartUser(HttpUser):
    wait_time = between(0.1, 1)

    @task(1)
    def submit_pfb(self):
        body = {"namespace_id": "0c204d39600fddd3", "data": "f1f20ca8007e910a3bf8b2e61da0f26bca07ef78717a6ea54165f5", "gas_limit": 80000, 
        "fee": 2000}
        headers = {'content-type':'application/json'}
        response = self.client.post("/submit_pfb", json = body, headers = headers, name = 'submit_pfb')
    
    


