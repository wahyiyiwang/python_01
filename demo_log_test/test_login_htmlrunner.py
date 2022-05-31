import unittest
import sys


from demo_log_test.HTMLTestRunner import HTMLTestRunner
from work.work3 import logink


class TestLogin(unittest.TestCase):

    #初始化方法
    @classmethod
    def setUpClass(self) -> None:
        print("开始运行方法：",sys._getframe().f_code.co_name)


    #清除方法
    @classmethod
    def tearDownClass(self) -> None:
        print("开始运行的方法:",sys._getframe().f_code.co_name)

    #测试登录的测试用例
    #case1：输入正确的用户名和正确的密码登录
    def test_login_sucess(self):
        except_value = 0
        actual_value = login('admin','123456').get('code')
        self.assertEqual(except_value,actual_value)

    #case2:输入错误的用户名和密码
    def test_user_wrong(self):
        except_value = 1
        actual_value = login('bac','12345').get('code')
        self.assertEqual(except_value,actual_value)

    #case3:输入空的密码
    def test_password_is_null(self):
        except_value = 1
        actual_value = login('admin','').get('code')
        self.assertEqual(except_value,actual_value)


if __name__ == '__main__':

    #创建一个套件a
    suite_a = unittest.TestSuite()
    suite_a.addTest(TestLogin('test_login_sucess'))
    suite_a.addTest(TestLogin('test_user_wrong'))
    suite_a.addTest(TestLogin('test_password_is_null'))
    print(suite_a)

    #创建一个测试报告文件，生成html文件
    test_report = './test_report.html'

    with open(test_report,'wb') as f:

        runner = HTMLTestRunner(f,title='测试报告',description='测试报告描述')
        runner.run(suite_a)