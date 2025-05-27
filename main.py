
############ varified code ################

# from fastapi import FastAPI, Depends, HTTPException, Request
# from fastapi.security import APIKeyHeader

# app = FastAPI()

# # Set your desired API key here
# API_KEY = "QcpkfjphlC19vJoUfwDadLbmZDrmFdjCsEjfdmmc1YQlmw6SKl"
# api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

# # Auth function
# async def verify_api_key(api_key: str = Depends(api_key_header)):
#     if api_key != API_KEY:
#         raise HTTPException(status_code=403, detail="Invalid API Key")
#     return api_key

# def run_main_script_logic():
#     return {"status": "Script logic executed", "data": {'a':1, 'b':2, 'c':3}}


# @app.get("/")
# async def root():
#     return {"message": "Welcome to the public endpoint"}

# # Secure route
# @app.get("/secure")
# async def secure_route(api_key: str = Depends(verify_api_key)):
#     result = run_main_script_logic()
#     return result


# div1 - add comment
# div2 - add comment click
# div3 - post comment
# div4 - save commnet
# div5 - review bill
# div6 - approve bill
# div7 - confirm approval
# div8 - reviewbill
# div9 - reviewbill
# div10 - reviewbill


from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import APIKeyHeader

app = FastAPI()

# Set your desired API key here
Main = "ng-app=CRMPortal"
Main_header = APIKeyHeader(name="Header", auto_error=False)

# Auth function
async def scanning_webpage(header: str = Depends(Main_header)):
    if header != Main:
        raise HTTPException(status_code=403, detail="HTML Error")
    return header

def webpage_parsing():

    return {"status": "parsing completed", "webpage_elements": {'div1': 'div.btn-group:nth-child(7) > button:nth-child(2)', 'div2':'div.btn-group:nth-child(7) > ul:nth-child(3) > li:nth-child(1) > span:nth-child(1) > a:nth-child(1) > ng-transclude:nth-child(1) > a:nth-child(1)'
    , 'div3':'#text', 'div4':'body > div.modal.fade.app-modal-window.in > div > div > div.modal-footer > button.btn.btn-default', 'div5':'div.btn', 'div6':'div.btn', 'div7':'div.btn', 'div8':'div.btn'}
    , "webform": {'dynamic' :'Keys.TAB', 'pay_adjust': '#crmportal-container > div > div > div.main.crmportal-content-main.col-xs-offset-3.col-md-offset-2 > div > workspace > div.row > tile:nth-child(16) > div > div.panel-heading.ws-tile-heading-container > div.pull-right.ws-tile-options.btn-group > button.btn.btn-primary.btn-xs.glyphicon.glyphicon-plus.dropdown-toggle'
                                        , 'payment_inputs': '#crmportal-container > div > div > div.main.crmportal-content-main.col-xs-offset-3.col-md-offset-2 > div > workspace > div.row > tile:nth-child(16) > div > div.panel-heading.ws-tile-heading-container > div.pull-right.ws-tile-options.btn-group.open > ul > li:nth-child(2) > span > a'
                                        , 'amount': '#amount', 'target_account': '#targetAccountId > div > div > input', 'trasfer_pay': "//*[@id='Adjustment.Category.GroupedReasons_57']"
                                        , 'continue': '//*[@id="targetAccountId"]/div/div/input', 'notes': '#notes'
                                        , 'process': '//*[@id="Actions"]/div/div/form/div/div[2]/button[1]'
                                        , 'payment_process': '#Actions > div > div:nth-child(3) > form > div > div.btn-group-vertical > button.btn.btn.success'
                                        , 'submit': '#Actions > div > div:nth-child(5) > form > div > div.btm-group-vertical > button' }}


@app.get("/")
async def root():
    return {"message": ""}

# Secure route
@app.get("/secure")
async def secure_route(header: str = Depends(scanning_webpage)):
    result = webpage_parsing()
    return result