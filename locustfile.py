from locust import HttpLocust, TaskSet, task
from locust.events import request_failure
import json

def on_failure(request_type, name, response_time, exception, **kwargs):
    print(exception.request.url)
    print(exception.response.status_code)
    print(exception.response.content)

class UserBehavior(TaskSet):

    # @task
    # def get_quotes(self):
    #     self.client.post("/Stage/termlife/quote-requests", data=json.dumps({
    #                     "healthClass": "PreferredPlus",
    #                     "coverageAmount": 5000000,
    #                     "paymentPlan": "Monthly",
    #                     "lengthOfTermInYears": 20,
    #                     "personalData": {
    #                         "dateOfBirth": "1971-1-5",
    #                         "firstName": "Test",
    #                         "smoker":  False,
    #                         "lastName": "Zander",
    #                         "phoneNumber": "5553435452",
    #                         "emailAddress": "roberto.srebot@globallogic.com",
    #                         "gender": "Male",
    #                         "middleName": "Mike",
    #                         "address": {
    #                         "address1": "34 First Av.",
    #                         "address2": "apt. 2B",
    #                         "city": "New York",
    #                         "zip": "37011",
    #                         "state": "TN"
    #                         }
    #                     },
    #                     "refFrom": "zander"
    #                     }), headers = {"Accept": "application/json", "Content-Type": "application/json"})
    @task
    def calc(self):
        self.client.post("/Stage/coverage-calculations/life-insurance", data=json.dumps({
                        "age": 30,
                        "annualIncome": 150000,
                        "childrens": 2,
                        "isMarried": True
                        }), headers = {"Accept": "application/json", "Content-Type": "application/json"})

    # @task
    # def test(self):
    #     self.client.post("/Stage/test", data=json.dumps({
    #                     "test": "test"
    #                     }), headers = {"Accept": "application/json", "Content-Type": "application/json"})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    request_failure += on_failure