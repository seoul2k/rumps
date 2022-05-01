import requests
import os
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 400)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel(self)
        label1.setText('搜索:')
        label1.move(30, 150)
        ql_b = QLineEdit(self)
        ql_b.move(100, 150)
        label2 = QLabel(self)
        label2.setText('第几页:')
        label2.move(250, 150)
        ql_a = QLineEdit(self)
        ql_a.move(300, 150)
        btn = QPushButton(self)
        btn.setText('确定')
        btn.move(200, 200)

        def qd():
            # baidu search
            try:

                url = 'http://www.baidu.com/s'
                wd = ql_b.text()
                end = int(ql_a.text())
                begin = int(ql_a.text())

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
                    'cookie': 'BIDUPSID=9F8FA3B0625768C6522AAF5644DF83A1; PSTM=1625317090; __yjs_duid=1_38e2767112a58778b3bcff5e3abf01101625547751916; BDUSS=d2aFJIVnE3THNRdm94WXpkamNCNVNJWlNjdVpxWEV0OVFTbXRYSDRVZ1ZTTE5oSUFBQUFBJCQAAAAAAAAAAAEAAAADRb4Bc2VvdWwxawAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABW7i2EVu4thYz; BDUSS_BFESS=d2aFJIVnE3THNRdm94WXpkamNCNVNJWlNjdVpxWEV0OVFTbXRYSDRVZ1ZTTE5oSUFBQUFBJCQAAAAAAAAAAAEAAAADRb4Bc2VvdWwxawAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABW7i2EVu4thYz; BAIDUID=9F8FA3B0625768C685866049BD18FBD2:SL=1:NR=50:FG=1; BDSFRCVID=ZZ-OJeC62Gnf2V6DDzuUhw9Vtm5rbsOTH6f309w9PLrWUXUQUwE1EG0Paf8g0KuMQ8EVogKKKgOTHICF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJFDoD-htC83H48k-4QEbbQH-UnLq-J222OZ04n-ah02JlO1jfOpKq_uMhJeXqQMW20jbn7m3UTdsq76Wh35K5tTQP6rLt-eLgT4KKJxbnFh_pbILP5ODjb-hUJiBMnMBan7alOIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_CDjKMDjoyeU5eetjK2CntsJOOaCvN8U7Oy4oWK441Dh6m2TQR366I5Jn5-MclepvoDh3o3M04X-o9-hvT-54e2p3FBUQJhUJHQft20b0qjJnRKfJa2bCfVR7jWhvvep72yMrTQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCDJ5kDJRufV-3HaJvhKRopMtOhq4tehHRZWUc9WDTm_DopfxP5ORoeBprDhhLlbxRphUnNK2vH-pPK5DOlMCn3j-OHK6OX04J3ybbQ3mkjbnnyfn02OPKz0T5YLt4syPRiKMRnWg5mKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJDJCFKbK-wDjKae5PyhUjJetnKaKr-B4baHJOoDDvcjKccy4LdjG500J3utbTRbb5R-U5Ejtb5Q4vFXUQW3-Aq54RaWaQt-nToJpQf8IQKhjJ_QfbQ0-RhqP-jW26aQnvT-J7JOpvobUnxyMFdQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ht6IefRAq_KL2fIv0jbICqRrHM-0SqxbXqhTzHmOZ0l8Ktq3_eCoKjxOU2RLAMht8LJ3LJ6raQh7mWIQthItw5TrmXbDi3J7PQlQf3R64KKJxKRLWeIJo5fcGeMLZhUJiBMnMBan7alOIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbRO4-TFaj5QWDf5; BDSFRCVID_BFESS=ZZ-OJeC62Gnf2V6DDzuUhw9Vtm5rbsOTH6f309w9PLrWUXUQUwE1EG0Paf8g0KuMQ8EVogKKKgOTHICF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tJFDoD-htC83H48k-4QEbbQH-UnLq-J222OZ04n-ah02JlO1jfOpKq_uMhJeXqQMW20jbn7m3UTdsq76Wh35K5tTQP6rLt-eLgT4KKJxbnFh_pbILP5ODjb-hUJiBMnMBan7alOIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_CDjKMDjoyeU5eetjK2CntsJOOaCvN8U7Oy4oWK441Dh6m2TQR366I5Jn5-MclepvoDh3o3M04X-o9-hvT-54e2p3FBUQJhUJHQft20b0qjJnRKfJa2bCfVR7jWhvvep72yMrTQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCDJ5kDJRufV-3HaJvhKRopMtOhq4tehHRZWUc9WDTm_DopfxP5ORoeBprDhhLlbxRphUnNK2vH-pPK5DOlMCn3j-OHK6OX04J3ybbQ3mkjbnnyfn02OPKz0T5YLt4syPRiKMRnWg5mKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJDJCFKbK-wDjKae5PyhUjJetnKaKr-B4baHJOoDDvcjKccy4LdjG500J3utbTRbb5R-U5Ejtb5Q4vFXUQW3-Aq54RaWaQt-nToJpQf8IQKhjJ_QfbQ0-RhqP-jW26aQnvT-J7JOpvobUnxyMFdQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ht6IefRAq_KL2fIv0jbICqRrHM-0SqxbXqhTzHmOZ0l8Ktq3_eCoKjxOU2RLAMht8LJ3LJ6raQh7mWIQthItw5TrmXbDi3J7PQlQf3R64KKJxKRLWeIJo5fcGeMLZhUJiBMnMBan7alOIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbRO4-TFaj5QWDf5; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=8500842505a02k005e1h6ssjh0r; delPer=0; PSINO=5; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_MWM2MWJjZGE4N2QyMmFkMTYwZTZkMzE4OTEzYjU1NTU5MWIyOTFjYjMxMmU0MzYwNzhmMTJhNDFlZTRhNGFkNGZjOTk0MzE3MzhkMjFjMzg1ZjI1YWY4MjJjNjhkOGMzMTdjMWM3NDZkYTA3Zjc3MmRjODQxZTg2M2YzOTQ5MmUxZmYyMTUyMDMyYTc2YzY5ZTQ0YzU1Y2VjZDIwZmRjMDg4MTFlYzJmZTA4YWFjN2U4YTRlNzk2OTUyYzMyNGQ2; H_PS_PSSID=36309_36367_34812_36165_34584_35979_36341_36074_36281_26350_22157_36061; BAIDUID_BFESS=AC051357BBC0A331B16E046CA3B0B41A:FG=1',
                    'referer': 'https://www.baidu.com/s?tn=02003390_43_hao_pg&isource=infinity&iname=baidu&itype=web&ie=utf-8&wd=1'
                }
                for page in range(begin, end+1):
                    pn = (page-1)*10
                    param = {
                        'wd': wd,
                        'pn': pn
                    }
                    response = requests.get(url, params=param, headers=headers)
                    file = str(page)+".html"
                    with open(file, 'w', encoding='utf-8') as fp:
                        print(response.text)
                        fp.write(response.text)
                    QMessageBox.information(
                        self, "消息框标题", "html路径:"+os.path.join(os.getcwd(), file), QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            except Exception as e:
                with open('error.html', 'w')as f:
                    f.write('''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>error:{}</title>
</head>

<body>
    <h1>error:{}</h1>
</body>

</html>
                    '''.format(e, e))
                QMessageBox.critical(
                    self, '标题', 'error:'+str(e), QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        btn.clicked.connect(qd)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
