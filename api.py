import requests
import os


class ExecApi:
    def __init__(self):
        response = requests.get(os.environ['EXERCISE_URL'],
                                headers={
                                    "X-RapidAPI-Key": os.environ['EXERCISE_API_KEY'],
                                    "X-RapidAPI-Host": os.environ['EXERCISE_HOST'],
                                })
        self._exercise = response.json()

    def get_exercises(self):
        return self._exercise

