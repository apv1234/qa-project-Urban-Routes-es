Name:
Proyecto Sprint 8 - Andrea Ponce Vera cohort_27

Project Description:

The objective of this project is to automate one of the happy paths of the Urban Routes application, specifically the process of successfully ordering a taxi with the comfort fare. The steps of the test will be described in more detail later.

Technologies Used:
The project utilizes the following libraries:

pytest: for executing the tests.
Selenium: as the programming language.

Execution Command:
- Ensure Python is installed. At the time of project creation, version 3.13 was used.
- Set up a functional base environment.
- Install the dependencies by running the following command from the project's root directory: pip install -r requirements
- Install pytest: pip install pytest
- In the configuration.py file, change the URL_SERVICE variable to the current and active Urban Routes server URL.
- Execute the tests from the console, where "root" is the base folder containing the project: pytest root/main.py

Instructions for Running Tests and Techniques Used:

To execute the tests, two main files are used:

- data.py: Contains the necessary data or inputs to run the tests. For example, the application's server URL, route data (from and to), card details, phone number, and message to the driver. These data can be modified as needed.
- main.py: Contains the defined libraries, locators, and elements used to execute the tests.

Locators and elements are grouped within the UrbanRoutesPage class.

Entry and exit hooks (setup_class and teardown_class), as well as the test cases, are grouped within the TestUrbanRoutes class.

The test cases are ordered according to the sequence of actions required to order a taxi with the Comfort fare. The steps are as follows:

1.Add route (from and to) – test_set_route
2.Select the fare – test_select_comfort_tariff
3.Enter phone number – test_ingresar_num_telef
4.Enter verification code – test_ingresar_codigo_SMS
5.Add card and CVV – test_agregar_tarjeta
6.Add message to driver – test_mensaje_conductor
7.Activate switch to request blanket and tissues – test_pedir_manta_panuelos
8.Order ice creams – test_pedir_dos_helados
9.Confirm order and reserve taxi – test_reservar_taxi

