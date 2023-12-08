# django-site
Set-ExecutionPolicy RemoteSigned -Scope Process
    quando nao executar automaticamente o codigo 
        .\venv\Scripts\Activate.ps1
 
aprendendo a usar o django curso do luizomf

.mypy_cache
    é uma extenção de analise de codigo(preciso adicionar ela

pasta venv 
    ambiente virtual

gitignore
    arquivo git

db.sqlite3
    arquivo de base de dados

manage.py
    arquivo que faz a mesma coisa que django-admin {ex: django-admin runserver/ python manage.py  runserver}  regra da casa é 
    utilizar o django-admin apenar para iniciar o startproject nome_do_projeto apenas
    apos isso utilizar manage.py 
    a diferença é que o manage.py configura a variavel de ambiente django_settings_module apontando para o arquivo settings.py do seu projeto django 


    pasta projeto1 
        criada por django-admin startproject projeto1 . ( o " . " é utilizado para criar a pasta sem criar novas pastas )

    __init__.py
        serve para indicar para o python que a pasta projeto é um pacote e para carregar coisas do pacote, como um export

    asgi.py e wsgi.py 
        ambos arquivos fazem referencia ao web server interface, usados para ligar o django ao servidor web externo (para produção)

    settings.py 
        configurações para mostrar pro django como se comportar
    
    urls.py
        porta de entrada para a aplicação

    