# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 00:40:11 2019

@author: higupta
"""

import configparser
config = configparser.ConfigParser()
# =============================================================================
# configuring the Html paths
# =============================================================================
config["MCP_Button"] = {'mcp_xpath': '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[4]/td[1]/div/ul/li/span[1]',
                          'mcp_xpath': '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[4]/td[1]/div/ul/li/span[1]'}

config["Propsal_action_1st_step"] = {'mcp_xpath': '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/div/ul/li/span[1]',
                                     'Jan_xpath': '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[4]/td[3]/div/div/h3/span',
                                     'Feb_xpath': '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[4]/td[4]/div/div/h3',
                                     'Mar_xpath': '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[4]/td[5]/div/div/h3',
                                     'Apr_xpath': '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[4]/td[5]/div/div/h3',
                                     'May_xpath': '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[4]/td[5]/div/div/h3/span',
                                     'Jun_xpath': '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[4]/td[5]/div/div/h3/span'}

config["Moving_quarter"] = {'arrow_xpath': '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/table/thead/tr/th[6]/div/span'}

config["Propsal_action_creation"] = {'ptype_xpath': '//*[@id="proposalType"]',
                                     'ptype_des_xpath': '//*[@id="newProposalForm"]/table/tbody/tr[1]/td/textarea'}

config["Add_Link"] = {'link_button' : '//*[@id="newProposalForm"]/table/tbody/tr[4]/td/button',
                      'link_addition': '//*[@id="newProposalForm"]/table/tbody/tr[4]/td/div/div[2]/input',
                      'link_des': '//*[@id="newProposalForm"]/table/tbody/tr[4]/td/div/div[1]/input',
                       'notes':   '//*[@id="newProposalForm"]/table/tbody/tr[6]/td/textarea' 
                        }

config['Create_proposal'] = {'create_button': '/html/body/div[2]/div/div[2]/div/div/div[3]/button[2]'
                            }

with open('EP_Automation\config\Html_paths.ini', 'w') as configfile:
      config.write(configfile)

# =============================================================================
# end
# =============================================================================
