from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sqlite3
from plyer import notification
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import schedule
import time
import difflib

conn = sqlite3.connect('url.db')
c = conn.cursor()
if c.execute('''select trim(replace(url, ' ', '_')) from url'''):    
    acquire_entries = c.fetchall()
if c.execute('''select trim(replace(name, ' ', '_')) from url'''):    
    acquire_names = c.fetchall()  
if c.execute('SELECT chk_number FROM url'):
    acquire_chknumbers = c.fetchall()  
if c.execute('SELECT chk_comits FROM url'):
    acquire_chkcomits = c.fetchall()  

conn = sqlite3.connect('url2.db')
c = conn.cursor()
if c.execute('''select trim(replace(email, ' ', '_')) from url2'''):    
    acquire_email = c.fetchone()  
if c.execute('''select trim(replace(password, ' ', '_')) from url2'''):    
    acquire_pass = c.fetchone()    
if c.execute('''select trim(replace(email2, ' ', '_')) from url2'''):    
    acquire_email2 = c.fetchone()    
if c.execute('''select trim(replace(password2, ' ', '_')) from url2'''):    
    acquire_pass2 = c.fetchone()                

def detect_updates_all():
    def detect_updates():
        for i in range(30):
            url = acquire_entries[i][0]
            name = acquire_names[i][0] 
            if acquire_chknumbers[i][0] == 1:
                if url.startswith('https://nuchs.blackboard.com/webapps/blackboard/content') or url.startswith('https://nuchs.blackboard.com/webapps/blackboard/execute'):
                    try:
                        options = Options()
                        options.add_argument('--headless')
                        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)                            
                        driver.get('https://nuchs.blackboard.com')
                        wait = WebDriverWait(driver, 10)
                        wait. until(EC.visibility_of_element_located((By.ID, 'redirectProvidersDropdownButton')))        
                        elem_redirectProvidersDropdownButton = driver.find_element_by_id('redirectProvidersDropdownButton')
                        elem_redirectProvidersDropdownButton.click()
                        wait. until(EC.visibility_of_element_located((By.ID, 'loginRedirectProviderList')))
                        elem_loginRedirectProviderList = driver.find_element_by_id('loginRedirectProviderList')
                        elem_loginRedirectProviderList.click()
                        wait. until(EC.visibility_of_element_located((By.ID, "i0116")))
                        driver.find_element_by_id("i0116").send_keys(acquire_email[0])
                        wait. until(EC.visibility_of_element_located((By.ID, "idSIButton9")))
                        driver.find_element_by_id("idSIButton9").click()
                        wait. until(EC.visibility_of_element_located((By.ID, "i0118")))
                        driver.find_element_by_id("i0118").send_keys(acquire_pass[0])
                        wait. until(EC.visibility_of_element_located((By.ID, "idSIButton9")))
                        driver.find_element_by_id("idSIButton9").click()
                        wait. until(EC.visibility_of_element_located((By.ID, "idSIButton9")))
                        driver.find_element_by_id("idSIButton9").click()   
                        if url.startswith('https://nuchs.blackboard.com/webapps/blackboard/content'):
                            driver.get(url)
                            wait.until(EC.visibility_of_element_located((By.ID, 'content_listContainer')))
                            new_elem = driver.find_element_by_xpath('//*[@id="content_listContainer"]').text
                        else:
                            driver.get(url)
                            wait.until(EC.visibility_of_element_located((By.ID, 'announcementList')))                    
                            new_elem = driver.find_element_by_xpath('//*[@id="announcementList"]').text                               

                        try:
                            with open(f'old_elem.txt({str(name)})', encoding='utf-8') as f:
                                old_elem = f.read() 
                        except:
                            old_elem = ''

                        if new_elem == old_elem:
                            print(f'{str(name)}:更新なし')
                        else:
                            with open(f'old_elem.txt({str(name)})', 'w', encoding='utf-8') as f:
                                f.write(new_elem) 

                            diff = difflib.Differ()     
                            output_diff = diff.compare(new_elem.split(), old_elem.split())           
                            for data in output_diff:
                                if data[0:1] in ['-']:
                                    new_data = data.replace('-', '')

                            notification.notify(
                                title=f"{str(name)}の内容が更新されました",
                                message=new_data,
                                app_name="Bb更新通知アプリ",
                                timeout=10
                            )
                        driver.close()        
                    except:
                        print('error')
                        driver.close()       
                else:
                    pass
            else:
                pass

    def detect_updates_comits():
        url1 = 'https://comits2.educ.chs.nihon-u.ac.jp/uniprove_pt/UnLoginAction'
        url2 = 'https://comits2.educ.chs.nihon-u.ac.jp/uniprove_pt/PMA020PLS01Action.do'
        if acquire_chkcomits[0][0] == 1:
            try:
                options = Options()
                options.add_argument('--headless')
                driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)                            
                driver.get(url1)
                wait = WebDriverWait(driver, 10)
                wait. until(EC.visibility_of_element_located((By.ID, 'userid')))  
                driver.find_element_by_id('userid').send_keys(acquire_email2[0])
                wait. until(EC.visibility_of_element_located((By.ID, 'password'))) 
                driver.find_element_by_id('password').send_keys(acquire_pass2[0])
                wait. until(EC.visibility_of_element_located((By.CLASS_NAME, "button_login")))
                driver.find_element_by_class_name("button_login").click()        
                driver.get(url2)
                wait. until(EC.visibility_of_element_located((By.CLASS_NAME, 'result'))) 
                new_elem = driver.find_element_by_xpath('//*[@id="contents_main"]/div[2]/div/div[2]/table').text
                try:
                    with open('old_elem.txt(COMITS)', encoding='utf-8') as f:
                        old_elem = f.read() 
                except:
                    old_elem = ''

                if new_elem == old_elem:
                    print('COMITS:更新なし')
                else:
                    with open('old_elem.txt(COMITS)', 'w', encoding='utf-8') as f:
                        f.write(new_elem) 
                        notification.notify(
                            title='Bb更新通知アプリ',
                            message="COMITSの内容が更新されました",
                            app_name="Bb更新通知アプリ",
                            timeout=10
                        )
                driver.close()        
            except:
                print('error')
                driver.close()
        else:
            pass
    detect_updates()
    detect_updates_comits()

def main():
    schedule.every(1).seconds.do(detect_updates_all)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
