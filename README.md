# 四川大学研究生教务系统一键自动评教脚本
## 安装
**chromedriver**

下载对应版本的[chromedriver](https://chromedriver.chromium.org/downloads)，本文件自带的版本为更新时最新版的驱动，版本号：122.0.6261.111

下载完成后在`evaluation.py`文件中以下代码中更改驱动的路径
```python
service = Service('./chromedriver.exe')
```
**selenium**
```bash
pip install selenium
```

## 用户信息
在`evaluation.py`文件中以下代码中添加用户信息，脚本可以在浏览器的登录页自动填充
```python
usrname = ''
password = ''
```
也可以选择在浏览器打开登录页的时候选择自己手动输入，在以下代码中更改跳转的等待时间
```python
# 等待输入验证码
time.sleep(7)
```

## 使用说明
运行脚本
```bash
python evaluation.py
```
等待脚本自动打开浏览器后，手动输入验证码，输入完毕后即可等待脚本运行（注：不需要点击登录按键，脚本会自动点击跳转，如果手动单击会因为提前跳转而运行失败）

## 评分参数更改
脚本中评分表中的选项为随机选择前两项，填写评语为‘老师讲的很好’，可以在代码中更改

**表单选项**

`.format()`中指定直接指定第几项
```python
choice_1 = driver.find_element(by=By.XPATH, value='//*[@id="nr_f9914f972dcf4bd4b847fb49f38a8757"]/div/label[{}]/span'.format(random.choice([1,2])))
choice_1.click()
```
**评语**

`.send_keys('老师讲的很好！')`中更改评语
```python
textarea.send_keys('老师讲的很好！')
textarea.send_keys(Keys.ENTER)
time.sleep(1)
```
