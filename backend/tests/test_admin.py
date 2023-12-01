from .base import BaseTestCase
from backend.models.system import UserInfo, Menu
from backend.core.extensions import db
from flask import url_for


class AdminTestCase(BaseTestCase):

    def fake_data(self):
        menu1 = Menu(id=1,  parent_id=0, menu_name='系统管理', menu_type='MENU',
                     menu_path='/system', component='Layout',
                     menu_visible=0,
                     menu_sort=1,
                     menu_icon='system',
                     redirect_url='/system/user'
                     )

        menu2 = Menu(id=2,
                     parent_id=1,
                     menu_name='菜单管理',
                     menu_type='CATALOG',
                     menu_path='menus',
                     component='system/menu/index',
                     menu_visible=0,
                     menu_sort=1,
                     menu_icon='menu',
                     )
        menu3 = Menu(
            id=3,
            parent_id=1,
            menu_name='/用户管理',
            menu_type='CATALOG',
            menu_path='/system',
            component='system/menu/user',
            menu_visible=True,
            menu_sort=3,
            menu_icon='user',
        )
        db.session.add(menu1)
        db.session.add(menu2)
        db.session.add(menu3)
        db.session.commit()

    def setUp(self):
        super(AdminTestCase, self).setUp()
        self.login()
        self.fake_data()
        # return super(AdminTestCase,self)
        return super().setUp()

    def test_api_index(self):
        response = self.client.get(url_for('api_v1.index'))
        data = response.get_json()
        self.assertEqual(data['api_version'], '1.0')
        self.get_oauth_token()

    def test_get_menus(self):
        self.fake_data()
        response = self.client.get(url_for('api_v1.menus'))
        data = response.get_json()
        self.assertEqual(data['code'], 'A230')
        pass

    def test_add_menus(self):
        token=self.get_oauth_token()
        response = self.client.post(url_for('api_v1.menus'), json=dict(
            id=5, parent_id=0,menu_path='/system',component='Layout', redirect_url='/test',
            menu_name='测试页',menu_icon='test', menu_type='MENU',menu_visible=0,
            menu_sort=4,menu_perm='perm'),headers=self.set_auth_headers(token=token) )

        data = response.get_json()

        self.assertIn('新增成功', data['msg'])
