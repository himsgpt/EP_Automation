# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 12:35:45 2019

@author: higupta
"""



def Automation():
    """
    Automating the process of creating an engagement plan
    """
    from selenium import webdriver
    import time
    import configparser
    import pandas as pd
    from datetime import datetime
    import global_var as g_var
    # =============================================================================
    # Input integration    
    # =============================================================================
    start_time = datetime.now()
    df = pd.read_excel(g_var.EXCEL_INPUT, encoding="ISO-8859-1", sheet_name = 'Main') 
    df.head(5)
    df.dtypes
    # =============================================================================
    # webdriver application
    # =============================================================================
    driver = webdriver.Chrome(g_var.CHROME_DRIVER_LOCATION)
    # click radio button
    driver.get(g_var.path)
    driver.implicitly_wait(20)
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, 1000)")
    driver.maximize_window()
    # =============================================================================
    #   leveraging Config file
    # =============================================================================
    config = configparser.ConfigParser()
    config.read('C:/Users/HIGUPTA/Downloads/Data_Science/Projects/EP_Automation/config/Html_paths.ini')   
    config.sections()
    
    """
    # =============================================================================
    # Client initiative
    # =============================================================================
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div/div[1]/ul/li/span').click()
    driver.find_element_by_link_text('NEW Client Initiative').click()
    # Cleint initiative name
    driver.find_element_by_xpath('//*[@id="newClientPgmForm"]/table/tbody/tr[1]/td[1]/input').send_keys('Test')
    # Client initiavtive outcome
    driver.find_element_by_xpath('//*[@id="newClientPgmForm"]/table/tbody/tr[2]/td[1]/textarea').send_keys('Test the outcome')
    
    
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[4]/td[1]/div/span/span[1]').click()
    
    # =============================================================================
    # KIs from  dropdown
    # =============================================================================
    driver.find_element_by_xpath('//*[@id="react-select-6--value"]/div[1]').click()
    element = driver.find_element_by_xpath('//*[@id="react-select-6--value"]/div[2]/input')
    element.send_keys('IT Operations Transformation')
    driver.find_element_by_xpath('//*[@id="react-select-5--value"]/div[1]').click() 
    
    # =============================================================================
    # MCP selection
    # =============================================================================
    try:
        driver.find_element_by_xpath('//*[@id="react-select-9--value"]/div[1]').click()
        driver.find_element_by_xpath('//*[@id="react-select-9--value"]/div[2]/input').send_keys('Moving towards highly efficient business management')
        driver.find_element_by_xpath('//*[@id="react-select-9--value"]/div[2]/input').send_keys(Keys.ENTER)
    except:
        driver.find_element_by_xpath('//*[@id="updateClientPgmForm"]/table/tbody/tr[3]/td[2]/div/div[2]/span[1]').click()
        driver.find_element_by_xpath('//*[@id="newMcpForm"]/fieldset/table/tbody/tr[1]/td/input').send_keys('Moving towards highly efficient business management')
        driver.find_element_by_xpath('//html/body/div[3]/div/div[2]/div/div/div[3]/button[2]').click()
    """
    # =============================================================================
    # Proposal action after KI slection
    # =============================================================================
    #click MCP button
    driver.find_element_by_xpath(config['Propsal_action_1st_step']['mcp_xpath']).click()
    driver.implicitly_wait(5)
    # =============================================================================
    # Check for month and click    
    # =============================================================================
    if (df['Select Month'][0]=='Jan'):
        new_proposal_xpath = 'jan_xpath'
    if (df['Select Month'][0]=='Feb'):
        new_proposal_xpath = 'feb_xpath'
    if (df['Select Month'][0]=='Mar'):
        new_proposal_xpath = 'mar_xpath'
        
    #Next Quarter
    if (df['Select Month'][0]=='Apr'):
        driver.find_element_by_xpath(config['Moving_quarter']['arrow_xpath']).click()
        new_proposal_xpath = 'apr_xpath'
    if (df['Select Month'][0]=='May'):
        driver.find_element_by_xpath(config['Moving_quarter']['arrow_xpath']).click()
        driver.find_element_by_xpath(config['Moving_quarter']['arrow_xpath']).click()
        new_proposal_xpath = 'may_xpath'
    if (df['Select Month'][0]=='Jun'):
        driver.find_element_by_xpath(config['Moving_quarter']['arrow_xpath']).click()
        driver.find_element_by_xpath(config['Moving_quarter']['arrow_xpath']).click()
        driver.find_element_by_xpath(config['Moving_quarter']['arrow_xpath']).click()
        new_proposal_xpath = 'jun_xpath'        
    
    driver.find_element_by_xpath(config['Propsal_action_1st_step'][new_proposal_xpath]).click()
    time.sleep(2)

    # =============================================================================
    # Proposal type selection 
    # =============================================================================
    # Locate and send keys directly
    User_proposal = df['Select Proposal Type'][0]
    driver.find_element_by_xpath(config['Propsal_action_creation']['ptype_xpath']).click()
    driver.find_element_by_link_text(User_proposal).click()
    
    #proposal description
    proposal_description = df['ACTIVITY_SUBJECT'][0]
    driver.find_element_by_xpath(config['Propsal_action_creation']['ptype_des_xpath']).send_keys(proposal_description)
    time.sleep(2)
    
    # =============================================================================
    # Link/Description
    # =============================================================================
    driver.execute_script("window.scrollTo(0, 1000)") 
    link_description = df['URL_TEXT'][0]
    link = df['URL_VALUE'][0]
    notes = "roadmap awating ahead"
    #click add link
    driver.find_element_by_xpath(config['Add_Link']['link_button']).click()
    #add link description
    driver.find_element_by_xpath(config['Add_Link']['link_addition']).send_keys(link)
    #add link
    driver.find_element_by_xpath(config['Add_Link']['link_des']).send_keys(link_description)
    #add notes
    driver.find_element_by_xpath(config['Add_Link']['notes']).send_keys(notes)
    time.sleep(5)
    # =============================================================================
    # Proposal creation
    # =============================================================================
    driver.find_element_by_xpath(config['Create_proposal']['create_button']).click()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    
Automation()
    
"""
Taking <60 seconds for 1 plan to be created
"""