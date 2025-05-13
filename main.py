import time
from cProfile import label

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    pedir_taxi_button = (By.CSS_SELECTOR, "button.button.round")

    comfort_tariff_option = (By.CSS_SELECTOR, ".tcard:nth-of-type(5)")
    comfort_tariff_title = [By.XPATH, "//div[@class='tcard - title' and text()='Comfort']"]

    num_tel_button = (By.CLASS_NAME, 'np-button')
    num_tel_field = (By.ID, 'phone')
    siguiente_nt_button = (By.CSS_SELECTOR, "button.button.full")
    introduce_code_field = (By.ID, 'code')
    confirmar_code_button = (By.CSS_SELECTOR, "#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button:nth-child(1)")

    metodo_pago_button = (By.CSS_SELECTOR, 'div.pp-button.filled')
    agregar_tarjeta_button = (By.CSS_SELECTOR, 'div.pp-row.disabled')
    num_tarjeta_field = (By.ID, 'number')
    codigo_field = (By.NAME, "code")
    agregar_button = (By.CSS_SELECTOR, "#root > div > div.payment-picker.open > div.modal.unusual > div.section.active.unusual > form > div.pp-buttons > button:nth-child(1)")
    #pregunta como obtenerlo
    cerrar_metodo_pago_button = (By.XPATH, "(//button[@class='close-button section-close'])[3]")

    mensaje_conductor_field = (By.ID, 'comment')
    manta_panuelos_checkbox = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]")
    agregar_helado = (By.CSS_SELECTOR, "div.counter-plus")
    reservar_taxi_button = (By.CSS_SELECTOR, 'div.smart-button-wrapper > button.smart-button')
    order_header_title = (By.CLASS_NAME, "order-header-title")

    def __init__(self, driver):
        self.driver = driver


    #Busca el campo from y escribe la direccion
    def set_from(self, address_from):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(address_from)

    # Busca el campo to y escribe la direccion
    def set_to(self, address_to):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.to_field))
        self.driver.find_element(*self.to_field).send_keys(address_to)

    #Regresa el valor del campo from
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    # Regresa el valor del campo to
    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    #Agrega la direccion, en este metodo se juntan los metodo escribe el campo from y to para facilitar el llamado de la accion
    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_pedir_taxi(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.pedir_taxi_button))
        self.driver.find_element(*self.pedir_taxi_button).click()

    def click_comfort(self):
        self.driver.find_element(*self.comfort_tariff_option).click()

    def click_num_telef(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.num_tel_button))
        self.driver.find_element(*self.num_tel_button).click()

    def ingresar_num_telef(self, phone_number):
        self.driver.find_element(*self.num_tel_field).send_keys(phone_number)

    # Regresa el valor del campo num_telef
    def get_num_telef(self):
            return self.driver.find_element(*self.num_tel_field).get_property('value')

    def click_siguiente_num(self):
        self.driver.find_element(*self.siguiente_nt_button).click()

    def ingresar_codigo(self, code):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.introduce_code_field))
        self.driver.find_element(*self.introduce_code_field).send_keys(code)

    # Regresa el valor del campo codigo
    def get_codigo(self):
            return self.driver.find_element(*self.introduce_code_field).get_property('value')

    def click_confirmar_code(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.confirmar_code_button))
        self.driver.find_element(*self.confirmar_code_button).click()

    def click_metodo_pago(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.metodo_pago_button))
        self.driver.find_element(*self.metodo_pago_button).click()

    def click_agregar_tarjeta(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.agregar_tarjeta_button))
        self.driver.find_element(*self.agregar_tarjeta_button).click()

    def ingresar_num_tarjeta(self, card_number):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.num_tarjeta_field))
        self.driver.find_element(*self.num_tarjeta_field).send_keys(card_number)
        self.driver.find_element(*self.num_tarjeta_field).send_keys(Keys.TAB)

    # Regresa el valor del campo num tarjeta
    def get_num_tarjeta(self):
            return self.driver.find_element(*self.num_tarjeta_field).get_property('value')

    def ingresar_num_card_code(self, card_code):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.codigo_field))
        self.driver.find_element(*self.codigo_field).send_keys(card_code)
        self.driver.find_element(*self.codigo_field).send_keys(Keys.TAB)

    # Regresa el valor del campo card code
    def get_num_card_code(self):
            return self.driver.find_element(*self.codigo_field).get_property('value')

    def click_boton_agregar(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.agregar_button))
        self.driver.find_element(*self.agregar_button).click()

    def click_boton_cerrar_metodo_pago(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.cerrar_metodo_pago_button))
        self.driver.find_element(*self.cerrar_metodo_pago_button).click()

    def mensaje_conductor(self, message_for_driver):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.mensaje_conductor_field))
        self.driver.find_element(*self.mensaje_conductor_field).send_keys(message_for_driver)

    # Regresa el valor del campo mensaje conductor
    def get_mensaje_conductor(self):
            return self.driver.find_element(*self.mensaje_conductor_field).get_property('value')

    def pedir_manta_panuelos(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.manta_panuelos_checkbox))
        self.driver.find_element(*self.manta_panuelos_checkbox).click()

    def pedir_dos_helados(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.agregar_helado))
        self.driver.find_element(*self.agregar_helado).click()
        self.driver.find_element(*self.agregar_helado).click()

    def reservar_taxi(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.reservar_taxi_button))
        self.driver.find_element(*self.reservar_taxi_button).click()



class TestUrbanRoutes:

    routes_page = None
    driver = None
    order_header_title = (By.CLASS_NAME, "order-header-title")
    manta_panuelos = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[1]")
    ice_cream = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]")


    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.start_session(capabilities)

        # NAVEGADOR
        cls.driver.get(data.urban_routes_url)
        # constructor (manda llamar la clase)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        WebDriverWait(self.driver,20)
        self.routes_page.click_pedir_taxi()
        self.routes_page.click_comfort()
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_ingresar_num_telef(self):
        phone_number = data.phone_number
        self.routes_page.click_num_telef()
        self.routes_page.ingresar_num_telef(phone_number)
        self.routes_page.click_siguiente_num()
        assert self.routes_page.get_num_telef() == phone_number

    def test_ingresar_codigo_SMS(self):
        code = retrieve_phone_code(driver = self.driver)
        self.routes_page.ingresar_codigo(code)
        WebDriverWait(self.driver, 20)
        self.routes_page.click_confirmar_code()
        assert self.routes_page.get_codigo() == code

    def test_agregar_tarjeta(self):
        card_number = data.card_number
        card_code = data.card_code
        self.routes_page.click_metodo_pago()
        self.routes_page.click_agregar_tarjeta()
        self.routes_page.ingresar_num_tarjeta(card_number)
        self.routes_page.ingresar_num_card_code(card_code)
        self.routes_page.click_boton_agregar()
        self.routes_page.click_boton_cerrar_metodo_pago()
        assert self.routes_page.get_num_tarjeta() == card_number
        assert self.routes_page.get_num_card_code() == card_code


    def test_mensaje_conductor(self):
        message_for_driver = data.message_for_driver
        self.routes_page.mensaje_conductor(message_for_driver)
        assert self.routes_page.get_mensaje_conductor() == message_for_driver


    def test_pedir_manta_panuelos(self):
        self.routes_page.pedir_manta_panuelos()
        label_name = self.driver.find_element(*self.manta_panuelos).text
        assert label_name == 'Blanket and handkerchiefs'


    def test_pedir_dos_helados(self):
        self.routes_page.pedir_dos_helados()
        label_ice_cream = self.driver.find_element(*self.ice_cream).text
        assert label_ice_cream == '2'



    def test_reservar_taxi(self):
        self.routes_page.reservar_taxi()
        WebDriverWait(self.driver, 50).until(expected_conditions.text_to_be_present_in_element(self.order_header_title, 'driver'))
        titulo = self.driver.find_element(*self.order_header_title).text
        assert 'driver' in titulo, "El título no contiene la palabra 'number'"
        time.sleep(5)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
