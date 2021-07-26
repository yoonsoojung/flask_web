from flask import Flask , render_template
from data import Articles

app = Flask(__name__)
# @ = 데코레이션
# return : 반환해준다
app.debug = True
#디버그 모드 restart  개발할 때만 쓰고 다 쓰고 나면 무조건 지워야 한다. 아니면 해킹의 대상이 된다.
@app.route('/', methods=['GET','POST'])
def hello_world():
    articles = Articles()
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run()