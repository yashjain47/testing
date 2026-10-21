Feature: OrangeHRM Logo
    Scenario: Login to orangehrm 
        Given launch chrome browser  
        When open orangehrm page
        And enter username "Admin" and password "admin123"
        And click on login button
        Then user must successfully login to the dashboard


    Scenario Outline: Login to orangehrm with Multiple Parameters 
        Given launch chrome browser  
        When open orangehrm page
        And enter username "<username>" and password "<password>"
        And click on login button
        Then user must successfully login to the dashboard

        Examples:
            | username | password |
            | admin    | admin123 | 
            | admin123 | admin    |
            | admin    |admin@123 |
            | abc      | admin123 |



