from fastapi import FastAPI
from fastapi import FastAPI, Form, Request

import uvicorn
from routers import user_router, home_router,wine_router,mbti_router

app = FastAPI()
app.include_router(user_router.router)
app.include_router(home_router.router)
app.include_router(wine_router.router)
app.include_router(mbti_router.router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)