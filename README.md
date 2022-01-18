# testefrexco
Desafio criação de API para Frexco.
## requerimentos de instalação
```bash
pip install -r requirements.txt
```
## Requerimentos para execução:
* Criar base de dados conforme o arquivo `settings.py`;
* Modificar usuário, senha e localização conforme desejar;
* Executar:
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
python manage.py loaddata fixture.json
```
```bash
python manage.py runserver
```
