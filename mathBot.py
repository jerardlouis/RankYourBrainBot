import selenium
from selenium import webdriver
import urllib
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

driver = webdriver.Chrome(executable_path=r"C:\\Users\\jguev\\Downloads\\chromedriver\\chromedriver")
#driver.get("https://rankyourbrain.com/mental-math/mental-math-test-easy")

driver.get("https://rankyourbrain.com/mental-math/mental-math-test-easy/play")
#time.sleep(25)
try:
    myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'beforeAnswer')))
    print("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")
#time.sleep(5)
timer = driver.find_element_by_id('counterTotal').text
while(timer != "00:00:02"):
    timer = driver.find_element_by_id('counterTotal').text
    print('time: ' + timer)
    problem = driver.find_element_by_id('beforeAnswer').text
    problem = problem[:-2]
    box = driver.find_element_by_id('answer')
    problem = problem.split(' ')
    print(problem)
    if '+' in problem:
        print('found add')
        print('a: ' + problem[0])
        print('b: ' + problem[-1])
        ans = str(add(int(problem[0]),int(problem[-1])))
        
    if '-' in problem:
        print('found subtract')
        print('a: ' + problem[0])
        print('b: ' + problem[-1])
        ans = str(subtract(int(problem[0]),int(problem[-1])))
    if '/' in problem:
        print('found divide')
        print('a: ' + problem[0])
        print('b: ' + problem[-1])
        ans = str(divide(int(problem[0]),int(problem[-1])))
    if '*' in problem:
        print('found multiply')
        print('a: ' + problem[0])
        print('b: ' + problem[-1])
        ans = str(multiply(int(problem[0]),int(problem[-1])))
    if '.' in ans:
        ans = ans.split('.')
    print(ans)
    box.send_keys(ans)

'''
<span id="beforeAnswer">93 - 63 = </span>
'''
'''
<input size="4" type="text" name="answer" id="answer">
'''