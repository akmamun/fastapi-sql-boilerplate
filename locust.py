import random
import string
from locust import HttpUser, task, between

class BoilerplateAPILoadTest(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def get_items(self):
        self.client.get("/v1/items")

    # @task
    # def write_item(self):
    #     random_data = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    #     payload = {"name": random_data}
    #     headers = {"Content-Type": "application/json"}
    #     self.client.post("/items", json=payload, headers=headers)
