from locust import HttpUser, task, between

class Remittance(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def gateway(self):
        res = self.client.get("/items")
