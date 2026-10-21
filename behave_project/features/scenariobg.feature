Feature: OrangeHRM Logo

    Background: common stepps
        Given launch chrome browser  
        When open orangehrm page
        And enter username "Admin" and password "admin123"
        And click on login button


    Scenario: Login to orangehrm 
        Then user must successfully login to the dashboard


    Scenario: Search User
        When navigate to search page
        Then search page should display

    Scenario: Advanced search user
        When navigate to advanced search page
        Then advanced search page should display

        