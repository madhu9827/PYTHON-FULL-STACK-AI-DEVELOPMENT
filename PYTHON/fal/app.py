from fastapi import FastAPI
#create fastapi
app=FastAPI()
@app.get('/')
def home_page():
    return{'msg':"home-page"}
@app.get('/about')
def about_page():
    return{'msg':"about-page"}
@app.get('/contact')
def contact_page():
    return{'msg':"contact-page"}