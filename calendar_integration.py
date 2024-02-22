import requests
import json
import msal
from flask import Flask, request

app = Flask(__name__)

# Configuración de la aplicación y permisos
client_id = '1184c22b-1a3d-4c43-9775-3c6581b20dbf'
client_secret = '-Sj8Q~6ZPCF3VcjBmA_foYM-inzOzSF7vyueNb4t'
scope = ['Calendars.ReadWrite']

# URL de la API de Graph para trabajar con eventos en el calendario
calendar_api_url = 'https://graph.microsoft.com/v1.0/me/calendar/events'

# Autenticación de usuario
app_auth = msal.ConfidentialClientApplication(
    client_id,
    authority='https://login.microsoftonline.com/common',
    client_credential=client_secret,
)

# Obtener URL de autorización
auth_url = app_auth.get_authorization_request_url(
    scopes=scope,
    redirect_uri='http://localhost:5000/callback',
)

print(f'Por favor, visita la siguiente URL para obtener el código de autorización: {auth_url}')

@app.route('/callback')
def callback():
    try:
        authorization_code = request.args.get('code')
        print(f'Código de autorización obtenido: {authorization_code}')

        # Obtener token de acceso usando el código de autorización
        token_response = app_auth.acquire_token_by_authorization_code(
            authorization_code,
            scopes=scope,
            redirect_uri='http://localhost:5000/callback',
        )

        access_token = token_response.get('access_token')
        print('Token de acceso:', access_token)

        # Crear un nuevo evento en el calendario
        event_data = {
            'subject': 'Reunion QA',
            'start': {
                'dateTime': '2024-02-23T08:00:00',
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': '2024-02-23T09:00:00',
                'timeZone': 'UTC',
            },
        }

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
        }

        # Hacer solicitud a la API de Microsoft Graph para crear un evento
        response_create = requests.post(calendar_api_url, headers=headers, json=event_data)

        if response_create.status_code == 201:
            print('Evento creado con éxito.')
        else:
            print('Error al crear el evento. Código de estado:', response_create.status_code)
            print('Respuesta del servidor:', response_create.text)

        # Obtener la lista de eventos
        response_get = requests.get(calendar_api_url, headers=headers)

        if response_get.status_code == 200:
            events = response_get.json()
            print('Eventos del calendario:')
            for event in events['value']:
                print('Título:', event.get('subject'))
                print('Inicio:', event.get('start').get('dateTime'))
                print('Fin:', event.get('end').get('dateTime'))
                print('---')
        else:
            print('Error al obtener eventos. Código de estado:', response_get.status_code)
            print('Respuesta del servidor:', response_get.text)

    except Exception as e:
        print(f"Error: {str(e)}")

    return 'Código de autorización obtenido. Puedes cerrar esta ventana.'

if __name__ == '__main__':
    app.run(port=5000)
