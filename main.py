from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def autorization():
    return FileResponse("application/templates/authorization.html")


@app.get("/orders")
async def orders():
    return FileResponse("application/templates/orders.html")

@app.get("/warehouse")
async def warehouse():
    return FileResponse("application/templates/warehouse.html")

@app.get("/carrier")
async def carrier():
    return FileResponse("application/templates/carrier.html")

@app.get("/rout")
async def rout():
    return FileResponse("application/templates/rout.html")

@app.get("/analysis")
async def analysis():
    return FileResponse("application/templates/analysis.html")
