# Django Blog

> Projeto pessoal para explorar os recursos do Django Admin. A ideia é utiliza-lo para gerenciar  não apenas os post, mas também as categorias e a moderação de comentários.

Algumas telas:
![](https://user-images.githubusercontent.com/63860290/87205630-45ee6100-c2de-11ea-91a6-c87e828c9d42.png)
![](https://user-images.githubusercontent.com/63860290/87205634-47b82480-c2de-11ea-9ae7-d3692cc52a47.png)
![](https://user-images.githubusercontent.com/63860290/87205557-1c353a00-c2de-11ea-94c8-762c331f1766.png)
### TECNOLOGIAS

- Python
- Django
- Bootstrap4

### EXECUTANDO PROJETO LOCALMENTE:

Clone o repositório.

```python
git clone https://github.com/veronicaasilva/django-crud-cbv.git
cd django-crud-cbv
```

Crie um virtualenv com Python 

```python
python3 -m venv venv
. venv/bin/activate
```

Instale as dependências.

```python
pip install -r requirements.txt
```

Crie o banco de dados:

```python
python manage.py migrate
```

Execute o servidor de desenvolvimento:

```python
python manage.py runserver
```
