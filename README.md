# Onix
Onix game project.

## How to start to create it

1. Crear el proyecto Django.
    ```bash
    ~$ django-admin startproject onix
    ```

2. Crear la app `core`.
    ```bash
    ~$ cd onix
    ~/onix$ python manage.py startapp core
    ```

3. Crear las vistas.
    ```bash
    ~/onix$ vi core/views.py
    ```
    ```python
    from django.shortcuts import render, HttpResponse

    # Create your views here.

    def home(request):
        return HttpResponse('Inicio')
    
    def contact(request):
        return HttpResponse('Contacto')
    ```

4. Crear las URLs. Primero crea un nuevo archivo `core/urls.py`.
    ```bash
    ~/onix$ vi core/urls.py
    ```
    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='home'),
        path('contact/', views.contact, name='contact'),
    ]
    ```
    ```bash
    ~/onix$ vi onix/urls.py
    ```
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        # Paths del core
        path('', include('core.urls')),
        # Paths del admin
        path('admin/', admin.site.urls),
    ]
    ```

5. Migrar el proyecto.
    ```bash
    ~/onix$ python manage.py migrate
    Operations to perform:
        Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
        Applying contenttypes.0001_initial... OK
        Applying auth.0001_initial... OK
        Applying admin.0001_initial... OK
        Applying admin.0002_logentry_remove_auto_add... OK
        Applying admin.0003_logentry_add_action_flag_choices... OK
        Applying contenttypes.0002_remove_content_type_name... OK
        Applying auth.0002_alter_permission_name_max_length... OK
        Applying auth.0003_alter_user_email_max_length... OK
        Applying auth.0004_alter_user_username_opts... OK
        Applying auth.0005_alter_user_last_login_null... OK
        Applying auth.0006_require_contenttypes_0002... OK
        Applying auth.0007_alter_validators_add_error_messages... OK
        Applying auth.0008_alter_user_username_max_length... OK
        Applying auth.0009_alter_user_last_name_max_length... OK
        Applying auth.0010_alter_group_name_max_length... OK
        Applying auth.0011_update_proxy_permissions... OK
        Applying sessions.0001_initial... OK
    ```
6. Iniciar el servidor.
    ```bash
    ~/onix$ python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    December 24, 2019 - 17:01:35
    Django version 2.2.9, using settings 'onix.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ```