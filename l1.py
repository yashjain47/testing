"""
BDD (Behaviour- Driven development)


pytest-bdd  >>  plugin
behave      >>  python bdd 


1.  Feature File    >>  contain multiple scenarios (.feature)
2.  Scenario        >>  contain multiple steps
3.  Steps           >>  Multiple steps to make an outcome


Gherkin >>  it is a human readable language.
Gherkin keywords:
    scenario:   Title/short description
    given   :   Precondition
    when    :   Some event
    then    :   Some outcome [Conclusion]
    and/but :   Continuation/condition/Steps


Example:    

    Feature:    OranheHRM login

    Scenario:   Logo Presence on orangeHRM home page
        Given:  I launch Chrome Browser
        When:   I open orangehrm page
        Then:   i verify the logo present on page

            
    Scenario:   Login to orangehrm 
        Given:  i launch chrome browser  
        When:   i open orangehrm page
        And:    enter username and password
        And:    click on login button
        Then:   user must successfully login to the dashboard

        
pip install behave selenium allure-behave

commands:

To run feature file :   behave
                        or 
                        behave project/features/myfeature.feature


To generate allure reports: behave -f allure_behave.formatter:AllureFormatter -o reports/ features/


To see the allure file: allure serve reports/

"""