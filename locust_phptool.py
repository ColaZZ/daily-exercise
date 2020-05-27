from locust import HttpLocust, TaskSet, task, between

class WebsiteTasks(TaskSet):
    def on_start(self):
        # self.client.post("/login", {
        #     "username": "test",
        #     "password": "123456"
        # })

        self.client.get("http://ipselect.xadxqz.com/apiip?ip=101.37.152.111&token=c617ca101495dd52e4a4afd2c01d552c")

    @task(2)
    def index(self):
        self.client.get("http://ipselect.xadxqz.com/apiip?ip=61.140.26.137&token=c617ca101495dd52e4a4afd2c01d552c")

    # @task(1)
    # def about(self):
    #     self.client.get("/about/")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://ipselect.xadxqz.com/"
    wait_time = between(5, 15)
    