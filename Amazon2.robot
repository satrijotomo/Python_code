*** Settings ***
Library  Selenium2Library

*** Variables ***
${BROWSER1}  chrome
${BROWSER2}  firefox

*** Test Cases ***
Chrome: User should be able to search for product and add it in Cart
    Open Browser  http://www.amazon.com  ${BROWSER1}
    wait until page contains  Your Amazon.com
    Input Text  id=twotabsearchtextbox  Ferrari 458
    sleep  1
    Click Button  xpath=//*[@id="nav-search"]/form/div[2]/div/input
    sleep  1
    Click Link  css=#result_1 > div > div:nth-child(3) > div:nth-child(1) > a
    click button    xpath=//*[@id="add-to-cart-button"]
    sleep  3
    close browser

Firefox: User should be able to search for product and add it in Cart
    Open Browser  http://www.amazon.com  ${BROWSER2}
    wait until page contains  Your Amazon.com
    Input Text  id=twotabsearchtextbox  Ferrari 458
    sleep  1
    Click Button  xpath=//*[@id="nav-search"]/form/div[2]/div/input
    sleep  1
    Click Link  css=#result_1 > div > div:nth-child(3) > div:nth-child(1) > a
    click button    xpath=//*[@id="add-to-cart-button"]
    sleep  3
    close browser


*** Keywords ***
