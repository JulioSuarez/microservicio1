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