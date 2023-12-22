from .base import BaseTestCase
from backend.core.extensions import db
from backend.models.filemodel import FileInfo
import urllib.parse
class FileTestCase(BaseTestCase):
    
    def fake_file(self):
        orginname='5f946ca7ce7e47638f8d972a0e52017d.md'
        local_file='README.md'
        fileinfo=FileInfo(orginname=orginname,localname=local_file,file_path='2023/12')
        db.session.add(fileinfo)
        db.session.commit()

    def setUp(self):
        super(FileTestCase, self).setUp()
        self.login()
        self.fake_file()
        # return super(AdminTestCase,self)
        return super().setUp()
    
    def test_upload(self):
        response=self.client.post('/file/upload',data={'file':open('README.md','rb')})
        data=response.get_json()
        self.assertEqual(data['code'],'200')
        self.assertEqual(data['message'],'文件保存成功')
        self.assertEqual(data['data']['name'],FileInfo.query.first().localname)

    def test_downlaod(self):
        self.test_upload()
        response=self.client.get('/file/download/README.md')
        #print(response.__dict__)
        # if response.status_code == 200:
        # # Decode the filename in case it's URL-encoded
        #     filename = urllib.parse.unquote(response.headers['Content-Disposition'].split('filename=')[1].strip('"'))
        # print(filename)
        # self.assertEqual(filename, 'README.md')
        # self.assertEqual(response.headers['Content-Type'], 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        # self.assertEqual(response.status_code,200)
        # self.assertEqual(response.headers['Content-Disposition'],'attachment; filename="README.md"')
        # self.assertEqual(response.headers['Content-Type'],'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
