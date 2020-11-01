from flask import Flask, render_template
from random import sample

app = Flask(__name__)

@app.route('/')
def main():
    return 'hello world'

#사람 수만큼 점심 메뉴 추천
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ["자장면",'짬뽕','라면','브리또','사과','찜닭']
    return f'{sample(menu,people)}'

@app.route('/show')
def show():
    #음식 사진을 static 폴더에 추가하고 menu에 집어 넣습니다
    #음식 메뉴 개수는 더 많아도 됩니다.
    menu = ['짜장면.png', '짬뽕.jpg']
    #음식 메뉴 1개를 뽑습니다.
    pickme = ''.join(sample(menu,1))
    #index.html 파일에 이미지를 불러옵니다.
    return render_template('index.html',food_img=pickme)
    
if __name__ == "__main__" :
    app.run(debug=True)