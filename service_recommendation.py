from flask import Flask, request, make_response, jsonify
import sqlite3, os, sys, json
import urllib.request
from openpyxl import load_workbook

app = Flask(__name__)

########################### 추천 ################################
# category1 function
def category1_recommend_function(category):
    # 리스트 가져오기
    conn = sqlite3.connect('./menulist.db')
    cs = conn.cursor()
    cs.execute("SELECT * FROM MENU WHERE category1 LIKE '%" + category + "%';")
    rows = cs.fetchall()
    
    # 난수 처리 후 추첨
    for row in rows:
        print(row)
    
    menu = ""
    return menu

# category2 SEARCH function
def category2_recommend_function(category):
    # 리스트 가져오기
    conn = sqlite3.connect('./menulist.db')
    cs = conn.cursor()
    cs.execute("SELECT * FROM MENU WHERE category2 LIKE '%" + category + "%';")
    rows = cs.fetchall()
    
    # 난수 처리 후 추첨
    for row in rows:
        print(row)
    
    menu = ""
    return menu

    
    
#  메뉴 추천 처리
def process_category_response(lunch_category):
    
    # search_function(lunch_category)
    # category1_recommend_function(lunch_category)
    
    ### CATEGORY1
    # CASE 1 한식
    if(lunch_category == "한식"):
        answer = "한식으로 점심 메뉴를 추천해드릴게요!"
    
    # CASE 2 일식
    elif(lunch_category == "일식"):
        answer = "일식으로 점심 메뉴를 추천해드릴게요!"
    
    # CASE 3 양식
    elif(lunch_category == "양식"):
        answer = "양식으로 점심 메뉴를 추천해드릴게요!"
    
    # CASE 3 분식
    elif(lunch_category == "분식"):
        answer = "분식으로 점심 메뉴를 추천해드릴게요!"
    
    # CASE 3 아시안
    elif(lunch_category == "양식"):
        answer = "아시안으로 점심 메뉴를 추천해드릴게요!"
    
    ### CATEGORY2
    # CASE 1 밥류
    elif(lunch_category == "밥류"):
        answer = "밥류로 점심 메뉴를 추천해드릴게요!"
    
    # CASE 2 면류
    elif(lunch_category == "밥류"):
        lunch_category = "밥"
        answer = "면류로 점심 메뉴를 추천해드릴게요!"
    
    # CASE 3 버거
    elif(lunch_category == "버거"):
        answer = "버거로 점심 메뉴를 추천해드릴게요!"
    
    # CASE 아무거나
    else:
        answer = "알겠습니다! 점심 메뉴를 추천해드릴게요!"
                
    
    return answer
