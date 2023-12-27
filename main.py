import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class BotSelenium:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    def OpcionChrome(self):
        # Configuración del navegador
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=3')
        options.add_argument("--incognito")

        # Aceptar automáticamente las cookies
        prefs = {"profile.default_content_setting_values.cookies": 2} 
        options.add_experimental_option("prefs", prefs)

        # Eliminar banner de consentimiento de cookies
        options.add_argument('--disable-features=CookieConsent')
        options.add_argument('--disable-blink-features=AutomationControlled')


        return options

    def GrupoSancorSeguros(self):
        # Obtener opciones de Chrome
        options = self.OpcionChrome()

        # Configurar el navegador con las opciones personalizadas
        driver = webdriver.Chrome(options=options)
        
        # Acceder a la URL
        
        driver.get("https://portalcobranzas.gruposancorseguros.com/PolicyBalance")
        time.sleep(50)
        # Encuentra los campos de usuario y contraseña y el botón de inicio de sesión
        campo_usuario = driver.find_element(By.NAME, 'username')
        campo_contraseña = driver.find_element(By.NAME, 'password')

        # Ingresa el usuario y la contraseña proporcionados al objeto
        campo_usuario.send_keys(self.usuario)
        campo_contraseña.send_keys(self.contraseña)
        
        # Encuentra y haz clic en el botón de inicio de sesión por el texto que contiene
        boton_iniciar_sesion = driver.find_element(By.XPATH, '//span[contains(text(), "Iniciar sesión")]')
        boton_iniciar_sesion.click()

        # Espera un momento para que la página se cargue (puedes ajustar el tiempo según sea necesario)
        driver.implicitly_wait(5)
        
        # Cierra el navegador al finalizar
        driver.quit()

# Ejemplo de uso
usuario = "50430Mauricio"
contraseña = "Broker.2023$$"
bot = BotSelenium(usuario, contraseña)
bot.GrupoSancorSeguros()
