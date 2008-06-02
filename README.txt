SugarCRMMonitor Summary
-----------------------

SugarCRMMonitor provides in depth monitoring for the SugarCRM web application.
This is accomplished through a detailed web transaction check that will login to
your SugarCRM web interface and step through a variety of checks verifying that
no errors are encountered. During these steps the time for each operation is
recorded along with the the time that SugarCRM reports that each page was
rendered in. This allows for visualization of application and network latency
side by side.


SugarCRMMonitor Features
------------------------

Web Application Fault Monitoring:
    * Login check
    * Accounts listing check
    * Individual account check
    * Logout check

Performance metrics:
    * Total transaction time
    * Login time (real and reported)
    * Account listing time (real and reported)
    * Account view time (real and reported)


SugarCRMMonitor Installation & Usage
------------------------------------

To begin monitoring your SugarCRM web application you should add a new device
named the host portion of your SugarCRM URL in the /Web/SugarCRM device class. For example, if you go to http://crm.mycompany.com/index.php to get to your
application you should name your device "crm.mycompany.com".

You should then go to this device's zProperties and set the following:
    * zSugarCRMBase: This is only required if your SugarCRM instance is under
        a specific sub-url such as /sugarcrm/. In this case your zSugarCRMBase
        would be "sugarcrm/" without the quotes.

    * zSugarCRMTestAccount: Set this to an account name that will show up on
        the first page of your global accounts list.

    * zSugarCRMUsername: Set this to a user in SugarCRM that has permission to
        view the test account that you just set.

    * zSugarCRMPassword: Set this to the password for the user you just set.

You will now see some SugarCRM specific graphs on the device's Perf tab. You
will also receive events if any part of the the web transaction fails.

