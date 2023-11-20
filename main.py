from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)

app.include_router(basic_auth_users.router)

app.include_router(jwt_auth_users.router)

app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", tags=["Root"])
async def root():
    return {"Hola FastAPI!"}

@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}

# token para delta space
# B5anJF9V_fhA8ZUFDbB11c9EbdEsMW5rrNQXnUsJL

# crear entorno virtual, escribit en la terminal:
#   python -m venv venv  
# activar entorno virtual
#   \venv\Scripts\activate

# crear requirements.txt
#   pip freeze > requirements.txt

# instalar dependencias
#   pip install -r requirements.txt

# levantar servidor uvicorn
#     uvicorn main:app --reload


# para el despliegue en aws ec2 ubuntu 22.04
#     sudo apt-get update
#     python3 -V
#     sudo apt-get install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
#     sudo apt-get install git
#     git clone https://github.com/JulioSuarez/microservicio1.git
#     cd microservicio1 
#     nodejs --version
#     npm --version
#     sudo apt-get install nodejs
#     sudo apt-get install npm
#     npm install
#     npm run build
#     sudo npm install pm2@latest -g
#     sudo pm2 list
#     sudo apt-get install python3-venv
#     python3 -m venv venv
#     source venv/bin/activate
#     pip install -r requirements.txt
#     pm2 start "uvicorn main:app --host 0.0.0.0" --name "microservicio"
#     pm2 list

# agregar una nueva regla en la instancia de aws para el puerto 8000 
# custom TCP, 8000, anywere, 0.0.0.0/0



#     sudo apt-get install nginx
#     sudo nano /etc/nginx/sites-available/fastapi
#     sudo ln -s /etc/nginx/sites-available/fastapi /etc/nginx/sites-enabled
#     sudo nano /etc/nginx/nginx.conf
#     sudo nginx -t
#     sudo systemctl restart nginx
#     sudo ufw allow 'Nginx Full'
#     sudo ufw delete allow 'Nginx HTTP'
#     sudo ufw allow ssh
#     sudo ufw enable
#     sudo ufw status
#     sudo systemctl restart nginx
#     sudo systemctl status nginx
#     sudo nano /etc/nginx/sites-available/fastapi