# Microsoft Graph Calendar Script

Este script en Python utiliza la API de Microsoft Graph para interactuar con eventos en el calendario del usuario. Permite la autenticación del usuario, la creación de nuevos eventos y la obtención de eventos existentes.

## Requisitos

- Python 3.x
- Paquetes requeridos (instalables a través de `pip`): `requests`, `msal`, `flask`

## Configuración

Antes de ejecutar el script, asegúrate de configurar correctamente las siguientes variables en el código:

- `client_id`: Identificador de la aplicación registrada en Azure AD.
- `client_secret`: Clave secreta de la aplicación.
- `scope`: Ámbito de permisos requeridos (en este ejemplo, se utiliza 'Calendars.ReadWrite').
- `calendar_api_url`: URL de la API de Microsoft Graph para trabajar con eventos en el calendario.

## Uso

1. Ejecuta el script. (python3 calendar_integration.py)
2. Visita la URL proporcionada para obtener el código de autorización.
3. Después de autorizar, el script creará un nuevo evento y mostrará la lista de eventos existentes.

## Aviso

Este script es un ejemplo educativo y puede necesitar ajustes según tus necesidades. Asegúrate de seguir las mejores prácticas de seguridad al manejar credenciales de aplicaciones.

