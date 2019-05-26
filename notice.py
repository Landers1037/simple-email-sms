# notice
import psutil
import json


class system:
    with open('service.json', 'r', encoding='utf8') as file:
        data = json.load(file)

    def spy(self):

        cpu = '内存占用率：' + str(psutil.virtual_memory().percent) + '%' + "\n" \
            + 'CPU占用率： ' + str(psutil.cpu_percent(0)) + '%'

        syslog = ''
        pids = psutil.pids()
        sysprocess = []
        try:
            for pid in pids:
                p = psutil.Process(pid)
                sysprocess.append(p.name())

            if not sysprocess:
                sysprocess.append('服务器出现错误')
        except:
            sysprocess.append('python抓取异常')

        for data in self.data["sysprocess"]:
            if data in sysprocess:
                syslog = syslog + data + ': ok' + '\n'
            else:
                syslog = syslog + data + ': bad' + '\n'

        statlog = cpu + '\n' + syslog
        return statlog
