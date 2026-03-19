# config.py

# Configurações do site / aplicativo
APP = {
    # Nome do site para a tag `<title>...</title>`
    'title': 'MyPyPad',

    # Nome / logo do site, em HTML, para a tag `.navbar-brand` e outros usos
    'name': 'My<i class="bi bi-filetype-py text-warning px-0"></i>Pad',

    # Chave secreta (48 caracteres)
    # Obtenha essa chave rodando `python keygen.py`
    'secret_key': '697ab25e2fe2dfd30ae3c9e0ba5a563d51d2a4733f3dc09e92b8f45144db89aa007d32b4d2fe0eed9027dcc3bbee7538',
}

# Configurações do banco de dados
DB = {
    'name' : 'database.db',
}

# Configurações dos cookies
COOKIE = {
    'livedays' : 30,
}

# Configurações do e-mail
MAIL = {
    # Boolean: True envia e-mails, False não envia 
    "send_contact": True,

    # Servidor SMTP e porta do Gmail / provedor
    "server": "smtp.gmail.com",
    "port": 587,

    # Conta de e-mail do administrador do site
    "username": "saturndiy@gmail.com",
    "admin_email": "saturndiy@gmail.com",
    
    # Acesse https://myaccount.google.com/apppasswords para gerar a senha de aplicativo abaixo
    "password": "sllb reor exgp rxax",
}
 