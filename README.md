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
    from django.shortcuts import render

    # Create your views here.

    def home(request):
        return render(request, 'core/home.html')

    def contact(request):
        return render(request, 'core/contact.html')
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

7. Crear directorios para las plantillas y los ficheros estáticos.
    ```bash
    ~/onix$ mkdir core/templates
    ~/onix$ mkdir core/templates/core
    ~/onix$ mkdir core/static
    ~/onix$ mkdir core/static/core
    ```

8. Crear las plantillas.
    ```bash
    ~/onix$ > core/templates/core/base.html
    ~/onix$ > core/templates/core/home.html
    ~/onix$ > core/templates/core/contact.html
    ```

9. Decirle a Django que cargue los templates y los ficheros estáticos añadiendo el directorio `core` a la lista `INSTALLED_APPS`.
    ```bash
    ~/onix$ vi onix/settings.py
    ```
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'core',
    ]
    ```

10. Crear la app `services`.
    ```bash
    ~/onix$ python manage.py startapp services
    ```

11. Crear el modelo y añadir la app `services` a `settings.py`.
    ```bash
    ~/onix$ vi services/models.py
    ```
    ```python
    from django.db import models

    # Create your models here.
    class Service(models.Model):
        title = models.CharField(max_length=200, verbose_name='Título')
        subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
        content = models.TextField(verbose_name='Contenido')
        image = models.ImageField(verbose_name='Imagen', upload_to='services')
        created = models.DateTimeField(auto_now_add=True, verbose_name='Fechad de creación')
        updated = models.DateTimeField(auto_now=True, verbose_name='Fechad de edición')

        class Meta:
            verbose_name = 'servicio'
            verbose_name_plural = 'servicios'
            ordering = ['-created']
        
        def __str__(self):
            return self.title
    ```
    ```bash
    ~/onix$ vi onix/settings.py
    ```
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'core',
        'services',
    ]
    ```

12. Preparar la migración.
    ```bash
    ~/onix$ python manage.py makemigrations
    Migrations for 'services':
    services/migrations/0001_initial.py
        - Create model Service
    ```

13. Migrar el proyecto.
    ```bash
    ~/onix$ python manage.py migrate
    Operations to perform:
        Apply all migrations: admin, auth, contenttypes, services, sessions
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
        Applying services.0001_initial... OK
        Applying sessions.0001_initial... OK
    ```

14. Crear superusuario de la consola de administración.
    ```bash
    ~/onix$ python manage.py createsuperuser
    Username (leave blank to use 'johndoe'): admin
    Email address: info@mail.org
    Password: 
    Password (again): 
    Superuser created successfully.
    ```

15. Hacer que la nueva app `services` esté disponible desde el penel de administración.
    ```bash
    ~/onix$ vi services/admin.py
    ```
    ```python
    from django.contrib import admin
    from .models import Service

    # Register your models here.
    class ServiceAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')

    admin.site.register(Service, ServiceAdmin)
    ```

16. Iniciar el servidor.
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

17. Traducir la app al español.
    ```bash
    ~/onix$ vi onix/settings.py
    ```
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'core',
        'services.apps.ServicesConfig',
    ]
    
    ...

    LANGUAGE_CODE = 'es'
    ```
    ```bash
    ~/onix$ vi services/apps.py
    ```
    ```python
    from django.apps import AppConfig


    class ServicesConfig(AppConfig):
        name = 'services'
        verbose_name = 'Gestor de servicios'
    ```