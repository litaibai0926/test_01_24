
# pytest框架的驱动文件
import pytest
import subprocess
pytest.main()
# allure generate 这是执行生成allure的命令  执行后的allure存放在temp下  -o 转换html 生产报告放在result/report下,--clean 每次生产都会清除之前的
subprocess.call('allure generate ./result/temp -o ./result/report --clean',shell=True)
# 自动打开本地生成的 allure转化成html的报告
subprocess.call('allure open -h 127.0.0.1 -p 8883 ./result/report',shell=True)

