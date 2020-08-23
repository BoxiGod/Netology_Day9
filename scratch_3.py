import requests
import time
from datetime import timedelta


class StackOverflow:

    def get_questions(self, tag, days):
        cur_time = int(time.time())
        request = "https://api.stackexchange.com/2.2/search?fromdate=" \
                  + str(cur_time-int(timedelta(days=days).total_seconds())) + "&todate=" + str(cur_time) \
                  + "&order=desc&sort=activity&tagged=" + tag + "&site=stackoverflow"
        questions = requests.get(request).json()
        return questions

if __name__ == '__main__':
    stackoverflow = StackOverflow()
    print(stackoverflow.get_questions("python", 2))
