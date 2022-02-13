# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 12:35:45 2019

@author: higupta
"""

from selenium import webdriver
import time
import configparser
import pandas as pd
from datetime import datetime
import EP_Automation.src.global_var as g_var
import numpy as np
import logging
import sys
import pymongo
import json


class Automation:
    '''
    Automation blueprint
    '''
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=g_var.LOG_FILE, filemode='w', 
                        format='%(name)s - %(levelname)s - %(message)s', level = logging.DEBUG)
    
    def __init__(self):
        self.logger.info("started")
      
# =============================================================================
# Automation code 
# =============================================================================
    def main(self):
    
    # Read Data from mongo
        myclient = pymongo.MongoClient('localhost',27017)
        mydb = myclient['ep_automation']
        mycol = mydb['ep_automation_input']
        documents = mycol.find({"is_parsed":0})
        for doc in documents:
            unique_id = doc['_id']
            filepath = doc['file_path']
            filename = doc['file_name']
            url = doc['URL']
            path = filepath + filename
            print(path)
            response = self.initiatives(path, url)
            if response:
                doc.update({'_id':unique_id}, 
                           {"$set": {
                                   "is_parsed":1}})           
                
    def initiatives(self,path, url):
    # =============================================================================
    # Input integration    
    # =============================================================================
            
        self.logger.info("Input Integration \n")
        try:
            #df = pd.read_excel(g_var.PHASE2, encoding="ISO-8859-1", sheet_name = 'Main') 
            df = pd.read_excel(path, encoding="ISO-8859-1", sheet_name='Main')
        except Exception as e:
            self.logger.critical("Unable to Load file" + str(e))
            sys.exit(0)
    # =============================================================================
    # leveraging Config file
    # =============================================================================
        print(111)    
        self.logger.info("leveraging Config file")
        try:
            config = configparser.ConfigParser()
        except Exception as e:
            self.logger.error("Unable to find config. file" + str(e))
            sys.exit(0)
        config.read(g_var.CONFIG)   
        config.sections()
        global i
        i=0
        for j in range(0,2):
    # =============================================================================
    # webdriver application
    # =============================================================================
            self.logger.info("webdriver application")
            try:
                driver = webdriver.Chrome(g_var.CHROME_DRIVER_LOCATION)
            except Exception as e:
                self.logger.error("Unable to Load chrome driver" + str(e))
                sys.exit(0)
            # click radio button
            #driver.get(g_var.path)
            driver.get(url)
            driver.implicitly_wait(20)
            time.sleep(10)
            driver.maximize_window()
            if (j==0):
                step = config['Propsal_action_1st_step']
            elif(j==1):
                driver.execute_script("window.scrollTo(0, 20)")
                step = config['Propsal_action_2nd_step']
            elif(j==2):
                driver.execute_script("window.scrollTo(0, 50)")
                step = config['Propsal_action_3rd_step'] 
                
            #click MCP button
            driver.find_element_by_xpath(step['mcp_xpath']).click()
            driver.implicitly_wait(5)
            i = self.testing(step,df,j,i,config,driver)
        
    
    def testing(self,step,df,j,i,config,driver):
        """
        Automating the process of creating an engagement plan
        """
      
#        if (j==1):
#           driver.execute_script("window.scrollTo(0, 20)")
        initiatives = 'Initiative_'+str(j+1)
        print("j-",j,"i-",i)
        
    # =============================================================================
    # Proposal action after KI slection
    # =============================================================================
        while (df['Client_inititative'][i]==initiatives):
    # =============================================================================
    # Check for month and click    
    # =============================================================================
            self.logger.info("ran loop for " + str(i))
            print("j-",j,"i-",i)
            self.arrow(config,df,i,driver)
#           elif ((np.isnan(df['Select Month'][i]))==True): 
            print(111)
            driver.find_element_by_xpath(step['proposal_xpath']).click()
            time.sleep(2)
            
    # =============================================================================
    # Proposal type selection 
    # =============================================================================
            # Locate and send keys directly
            self.logger.info("proposal type selection")
            User_proposal = df['Select Proposal Type'][i]
            driver.find_element_by_xpath(config['Propsal_action_creation']['ptype_xpath']).click()
            driver.find_element_by_link_text(User_proposal).click()
            
            #proposal description
            proposal_description = df['ACTIVITY_SUBJECT'][i]
            driver.find_element_by_xpath(config['Propsal_action_creation']['ptype_des_xpath']).send_keys(proposal_description)
            time.sleep(2)
        
    # =============================================================================
    # Link/Description
    # =============================================================================
            self.logger.info("link type/description selection")        
            driver.execute_script("window.scrollTo(0, 1000)") 
            link_description = df['URL_TEXT'][i]
            link = df['URL_VALUE'][i]
            notes = df["Enter Your contact URL"][1]
            #click add link
            driver.find_element_by_xpath(config['Add_Link']['link_button']).click()
            #add link description
            driver.find_element_by_xpath(config['Add_Link']['link_addition']).send_keys(link)
            #add link
            driver.find_element_by_xpath(config['Add_Link']['link_des']).send_keys(link_description)
            #add notes
            driver.find_element_by_xpath(config['Add_Link']['notes']).send_keys(notes)
            time.sleep(2)
            
    # =============================================================================
    # Proposal creation
    # ============================= ================================================
            self.logger.info("Proposal creation")        
            driver.find_element_by_xpath(config['Create_proposal']['create_button']).click()
#            end_time = datetime.now()
#            self.logger.info('Duration: {}'.format(end_time - start_time))
            time.sleep(5)
            if (j==0 or j==1):
                driver.execute_script("window.scrollTo(0, 0)")
            else:
                driver.execute_script("window.scrollTo(0, 50)")
            i = i+1
        driver.close()
        return i
    
# =============================================================================
#     Arrow function
# =============================================================================
    def arrow(self,config,df,i,driver):
        """
        Transitioning into next month
        """
       # global config,df, i
        month = driver.find_element_by_xpath('//*[@id="calendarMonthselector"]').text
        print(month)
        while (df['Select Month'][i]!=month):
            driver.find_element_by_xpath(config['Moving_quarter']['arrow_xpath']).click()
            month = driver.find_element_by_xpath('//*[@id="calendarMonthselector"]').text
            
if __name__ == "__main__":
    Automation_obj = Automation()
    Automation_obj.main()
     
    