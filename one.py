from locust import HttpUser, constant, task


class MyReqRes(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(1)

    @task
    def get_user(self):
        self.client.get("/api/users?page=2")

    @task
    def create_user(self):
        self.client.post("/api/user", data='''
        {"name":"morpheus", "job":"Leader"}
        ''')
