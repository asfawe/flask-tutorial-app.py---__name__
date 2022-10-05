from flask import Flask
app = Flask(__name__) # 플라스크 애플리케이션을 생성하는 코드다. 코드에서 __name__ 이라는 변수에는 모듈명이 담긴다.
# 이 파일이 실행되면 pybo.py라는 모듈이 실행되는 것이므로 __name__ 변수에는 'pybo'라는 문자열이 담긴다.
# @app.route는 특정 주소에 접속하면 바로 다음 줄에 있는 함수를 호출하는 플라스크의 테코레이터다.

@app.route('/')
def hello_pybo():
    return 'Hello, Pybo!'