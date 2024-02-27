from datetime import datetime
from sqlalchemy import select,func
from backend.core.extensions import db
from backend.models.system import UserInfo,Menu,SysUserRole,SysRoleMenu,SysRole
from backend.models.scantool import CustomerInfo

def fake_admin():
    user=UserInfo(
        userno='admin',
        username='admin',
        password='123456',
    )
    db.session.add(user)
    db.session.commit()

def fake_menu():
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

def fake_role():
    role=SysRole(
        role_name='超级管理员',
        code='admin',
        create_user='admin',
        create_date=datetime.now(),
        last_modification_time=datetime.now(),
    )
    db.session.add(role)
    db.session.commit()

def fake_role_menu():
    role=db.session.query(SysRole).scalar()
    role_id=role.id
    role1=SysRoleMenu(
        role_id=role_id,
        menu_id=1,
    )
    role2=SysRoleMenu(
        role_id=role_id,
        menu_id=2,
    )
    role3=SysRoleMenu(
        role_id=role_id,
        menu_id=3,
    )
    db.session.add(role1)
    db.session.add(role2)
    db.session.add(role3)
    db.session.commit()


def fake_customer_info():
    data=[
        {
            "agent": "亚美斯通",
            "chipNo": "SIV6001SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "47160171",
            "id": 3,
            "isDeleted": False
        },
        {
            "agent": "亚美斯通",
            "chipNo": "SIV6002SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "47160172",
            "id": 4,
            "isDeleted": False
        },
        {
            "agent": "亚美斯通",
            "chipNo": "SIV6004SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "47160173",
            "id": 5,
            "isDeleted": False
        },
        {
            "agent": "亚美斯通",
            "chipNo": "SIV6011SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "47160174",
            "id": 6,
            "isDeleted": False
        },
        {
            "agent": "亚美斯通",
            "chipNo": "SIV6005SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "47160175",
            "id": 7,
            "isDeleted": False
        },
        {
            "agent": "亚美斯通",
            "chipNo": "SIV6006SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "47160176",
            "id": 8,
            "isDeleted": False
        },
        {
            "agent": "亚美斯通",
            "chipNo": "SIV6009SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "47160178",
            "id": 9,
            "isDeleted": False
        },
        {
            "agent": "亚美斯通",
            "chipNo": "SIV6010SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "47160179",
            "id": 10,
            "isDeleted": False
        },
        {
            "agent": "亚美斯通",
            "chipNo": "SIV6013SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "47160180",
            "id": 11,
            "isDeleted": False
        },
        {
            "agent": "亚美斯通",
            "chipNo": "SIV6019SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99014HLR",
            "id": 12,
            "isDeleted": False
        },
        {
            "agent": "亚美斯通",
            "chipNo": "SIV6020SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99014HMA",
            "id": 13,
            "isDeleted": False
        },
        {
            "agent": "亚美斯通",
            "chipNo": "SIV6001SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99014RYQ",
            "id": 14,
            "isDeleted": False
        },
        {
            "agent": "广东亿安仓供应链科技有限公司",
            "chipNo": "SIS037SP4",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99014VJX",
            "id": 16,
            "isDeleted": False
        },
        {
            "agent": "广东亿安仓供应链科技有限公司",
            "chipNo": "SIA068SP2",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99014WYG",
            "id": 17,
            "isDeleted": False
        },
        {
            "agent": "华为技术有限公司",
            "chipNo": "SIA068SP2",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99014WYG",
            "id": 18,
            "isDeleted": False
        },
        {
            "agent": "深圳中电港技术股份有限公司",
            "chipNo": "SID001SP3",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99015APV",
            "id": 19,
            "isDeleted": False
        },
        {
            "agent": "广东亿安仓供应链科技有限公司",
            "chipNo": "S1S252SP3",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99016QLS",
            "id": 20,
            "isDeleted": False
        },
        {
            "agent": "广东亿安仓供应链科技有限公司",
            "chipNo": "SIS252SP3",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99016QLS",
            "id": 22,
            "isDeleted": False
        },
        {
            "agent": "广东亿安仓供应链科技有限公司",
            "chipNo": "SIM195SP2C",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99016QLT",
            "id": 24,
            "isDeleted": False
        },
        {
            "agent": "广东亿安仓供应链科技有限公司",
            "chipNo": "SIAT116ASP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99016QLV",
            "id": 26,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航",
            "chipNo": "SIV6004SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99120312",
            "id": 27,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航",
            "chipNo": "SIV6011SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99120453",
            "id": 28,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航",
            "chipNo": "SIV6005SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99120455",
            "id": 29,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航",
            "chipNo": "SIV6009SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99120457",
            "id": 30,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航",
            "chipNo": "SIV6010SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99120459",
            "id": 31,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航",
            "chipNo": "SIV6002SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99120FKK",
            "id": 32,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航",
            "chipNo": "SIV6006SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99120FKL",
            "id": 33,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航",
            "chipNo": "SIV6001SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99120FYY",
            "id": 34,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航",
            "chipNo": "SIP017SP4",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99120KAF",
            "id": 35,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航电子科技有限公司",
            "chipNo": "SIA068SP2",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99120KEU",
            "id": 36,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航电子科技有限公司",
            "chipNo": "SISP160SP4",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99120KJG",
            "id": 37,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航电子科技有限公司",
            "chipNo": "SISP170SP5",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99120KJH",
            "id": 38,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航电子科技有限公司",
            "chipNo": "SIS032SP3",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99122950",
            "id": 39,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航电子科技有限公司",
            "chipNo": "SIA070SP2",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "99123223",
            "id": 40,
            "isDeleted": False
        },
        {
            "agent": "九江昕辰科技有限责任公司",
            "chipNo": "SIA072",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "XC1001",
            "id": 42,
            "isDeleted": False
        },
        {
            "agent": "九江昕辰科技有限责任公司",
            "chipNo": "SIV103",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "XC1002",
            "id": 43,
            "isDeleted": False
        },
        {
            "agent": "九江昕辰科技有限责任公司",
            "chipNo": "SIPL186SP3",
            "createData": "Mon, 01 Jan 1900 00:00:00 GMT",
            "createUser": "",
            "customerNo": "XC2001",
            "id": 44,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航电子科技有限公司",
            "chipNo": "SICG256SP3",
            "createData": "Fri, 24 Nov 2023 06:22:32 GMT",
            "createUser": "37AE20E0-3A7F-4AEE-90E8-6962651E5CC5",
            "customerNo": "99127290",
            "id": 51,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航电子科技有限公司",
            "chipNo": "SICG257SP3",
            "createData": "Fri, 24 Nov 2023 06:22:52 GMT",
            "createUser": "37AE20E0-3A7F-4AEE-90E8-6962651E5CC5",
            "customerNo": "99128244",
            "id": 52,
            "isDeleted": False
        },
        {
            "agent": "异常条码测试",
            "chipNo": "1PSIA070SP2",
            "createData": "Thu, 14 Dec 2023 03:16:25 GMT",
            "createUser": "5230E839-8491-4AFD-8C97-46F72906A47A",
            "customerNo": "/",
            "id": 53,
            "isDeleted": False
        },
        {
            "agent": "广东亿安仓供应链科技有限公司",
            "chipNo": "SIA077SP5",
            "createData": "Fri, 15 Dec 2023 07:19:45 GMT",
            "createUser": "5230E839-8491-4AFD-8C97-46F72906A47A",
            "customerNo": "99014VJU",
            "id": 54,
            "isDeleted": False
        },
        {
            "agent": "广东亿安仓供应链科技有限公司",
            "chipNo": "SIA071SP3",
            "createData": "Fri, 15 Dec 2023 07:22:45 GMT",
            "createUser": "5230E839-8491-4AFD-8C97-46F72906A47A",
            "customerNo": "99014YSC",
            "id": 55,
            "isDeleted": False
        },
        {
            "agent": "广东亿安仓供应链科技有限公司",
            "chipNo": "S1A078SP5",
            "createData": "Fri, 15 Dec 2023 07:23:31 GMT",
            "createUser": "5230E839-8491-4AFD-8C97-46F72906A47A",
            "customerNo": "99014YSK",
            "id": 56,
            "isDeleted": False
        },
        {
            "agent": "广东亿安仓供应链科技有限公司",
            "chipNo": "SIA078SP5",
            "createData": "Fri, 15 Dec 2023 07:23:53 GMT",
            "createUser": "5230E839-8491-4AFD-8C97-46F72906A47A",
            "customerNo": "99014YSK",
            "id": 57,
            "isDeleted": False
        },
        {
            "agent": "广东亿安仓供应链科技有限公司",
            "chipNo": "SIA070SP2",
            "createData": "Thu, 21 Dec 2023 06:15:48 GMT",
            "createUser": "5230E839-8491-4AFD-8C97-46F72906A47A",
            "customerNo": "99014YS]",
            "id": 58,
            "isDeleted": False
        },
        {
            "agent": "广东亿安仓供应链科技有限公司",
            "chipNo": "SIA070SP2",
            "createData": "Thu, 21 Dec 2023 06:16:42 GMT",
            "createUser": "5230E839-8491-4AFD-8C97-46F72906A47A",
            "customerNo": "99014YSJ",
            "id": 59,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航电子科技有限公司 ",
            "chipNo": "SID182SP3",
            "createData": "Wed, 03 Jan 2024 02:32:43 GMT",
            "createUser": "5230E839-8491-4AFD-8C97-46F72906A47A",
            "customerNo": "99128257",
            "id": 60,
            "isDeleted": False
        },
        {
            "agent": "深圳市亚美斯通电子有限公司",
            "chipNo": "SIA075SP4",
            "createData": "Thu, 11 Jan 2024 06:33:20 GMT",
            "createUser": "5230E839-8491-4AFD-8C97-46F72906A47A",
            "customerNo": "/",
            "id": 61,
            "isDeleted": False
        },
        {
            "agent": "深圳市亚美斯通电子有限公司",
            "chipNo": "SIA3024SP3",
            "createData": "Thu, 11 Jan 2024 07:01:48 GMT",
            "createUser": "5230E839-8491-4AFD-8C97-46F72906A47A",
            "customerNo": "/",
            "id": 62,
            "isDeleted": False
        },
        {
            "agent": "深圳市博智航电子科技有限公司",
            "chipNo": "SIP279SP4",
            "createData": "Fri, 19 Jan 2024 07:08:05 GMT",
            "createUser": "5230E839-8491-4AFD-8C97-46F72906A47A",
            "customerNo": "99128607",
            "id": 63,
            "isDeleted": False
        },
        {
            "agent": "深圳市亚美斯通电子有限公司",
            "chipNo": "SIA072SP5",
            "createData": "Fri, 02 Feb 2024 06:38:36 GMT",
            "createUser": "5230E839-8491-4AFD-8C97-46F72906A47A",
            "customerNo": "/",
            "id": 64,
            "isDeleted": False
        },
        {
            "agent": "深圳市亚美斯通电子有限公司",
            "chipNo": "SID182SP3",
            "createData": "Mon, 19 Feb 2024 07:00:32 GMT",
            "createUser": "5230E839-8491-4AFD-8C97-46F72906A47A",
            "customerNo": "/",
            "id": 65,
            "isDeleted": False
        }
    ]
    for i in data:
        cus=CustomerInfo(
            agent=i['agent'],
            chipNo=i['chipNo'],
            customerNo=i['customerNo'],
           
            createUser=i['createUser'],
            isDeleted=i['isDeleted']
        )
        db.session.add(cus)
        db.session.commit()

def fake_user_role():
    user_role=SysUserRole(
        user_id=1,
        role_id=1,
    )
    db.session.add(user_role)
    db.session.commit()