from time import sleep, time
from objectpage.login_page import LoginPage
from data.data import ReadWrite
from log.log import logger
import allure

'''
以上的类应该是导进来，注释以后运行脚本不能正常加载测试用例

不注释的话，则可以正常加载测试用例

'''


@allure.feature('登录模块')  # feature 是用来放模块的
class TestCases():
    @allure.story('登录成功的测试用例')
    def test_01(self, login):
        '''
         验证：用户输入正确账号密码可以正常登录
        '''
        print("验证第一条")
        with allure.step('驱动浏览器，读取excel中存储的账号和密码'):
            print('这是第一步')
        self.driver = login
        self.loginpage = LoginPage(self.driver)
        user_list = ReadWrite().excelread('users')  # 读取'users'这张sheet页的数据
        username = user_list[0][0]  # excel表的第0列的第0位就是用户名
        password = user_list[0][1]  # excel表的第0列的第1位就是密码
        with allure.step('读取excel中存储的账号和密码后，输入账号密码'):
            print('这是第二步')
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        with allure.step('点击登录'):
            print('这是第三步')
        self.loginpage.click_login()
        sleep(1)
        # try:
        with allure.step('登录成功后，断言判断是否成功'):
            print('这是第4步')
        assert '我的地盘 - 禅道' in self.driver.title  # 断言判断登录成功后的页面，我的地盘 - 禅道 是不是在浏览器标题中
        self.loginpage.click_logout()
        with allure.step('断言正确，打印成功登录信息'):
            print('这是第5步')
        logger.info('有效的用户名和密码登录成功')
        # except:
        #     print("登录页面不显示")

    @allure.story('登录失败的测试用例')
    def test_02(self,login):
        '''
         验证：用户输入密码为空时，登录失败
        '''
        with allure.step('驱动浏览器'):
            print('第一步')
        self.driver = login
        self.loginpage = LoginPage(self.driver)
        with allure.step('输入账号'):
            print('第二步')
        self.loginpage.input_username('admin')
        with allure.step('不输入密码，直接点击登录'):
            print('第三步')
        self.loginpage.click_login()
        sleep(2)
        with allure.step('出来弹窗'):
            print('第四步')
        alert_login = self.driver.switch_to.alert
        alert_login.accept()
        print("验证第二条")
