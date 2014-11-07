from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # El ususario va a la pagina del CRM de USA-EJH
        self.browser.get('http://localhost:8000')
        self.assertIn('CRM EJH-USA', self.browser.title)

        # Ingresa sus credenciales de acceso
        inputbox = self.browser.find_element_by_id('id_usuario')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                        'Usuario')
        inputbox.send_keys('prueba')

        inputbox = self.browser.find_element_by_id('id_password')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                        'Password')
        inputbox.send_keys('1234')

        inputbox.send_keys(Keys.ENTER)
                        
        # Dependiendo de su perfil (grupo) puede ver el menu de opciones para capturar
        # modificar o eliminar informacion
        

# Becarios: pueden capturar datos de prospectos y realizar llamadas a prospectos

# Responsables: Becarios, preparatorias (modificar), eventos (crear)

# Directivos: Prospectos, eventos, preparatorias (consulta). Reportes.

if __name__ == '__main__':
    unittest.main(warnings='ignore')


