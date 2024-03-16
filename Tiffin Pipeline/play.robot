*** Settings ***
Library     SeleniumLibrary
*** Test Cases ***
Mytest
    open browser    https://www.youtube.com/watch?v=wiurYrCDKyI  chrome
    sleep   7
    Press Keys   xpath=//body    k
#    Wait Until Element Is Visible    class:ytp-ad-text ytp-ad-skip-button-text      15      None
    sleep   200 minutes 10 seconds

