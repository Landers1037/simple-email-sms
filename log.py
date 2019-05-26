# log
import json


class pylog():

    def logout(self, data):
        with open('log.json', 'w', encoding='utf8') as f:
            json.dump(data, f, indent=4)
