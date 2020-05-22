from flask import Flask,url_for,request,render_template,send_from_directory
from datetime import timedelta
app  =  Flask(__name__)
app.config['DEBUG']=True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
msg=""

@app.route('/')
def mainpage():
    return render_template('mainpage.html')

@app.route('/predit')
def Predit():
    print("进入预测页面")
    return render_template('extendPredit.html')

@app.route('/predit', methods=['POST', 'GET'])
def Resquest():
    print("收到请求")
    if request.method == 'POST':
        msg = request.form['word']
        print("收到POST ",)
        #request.form['word']
        create_txt(msg)
        return render_template('extendPredit.html',output=request.form['word'])

@app.route("/download")
def download1():
    print("下载")

    return send_from_directory(r".\\static\\resource", filename="识别结果.txt", as_attachment=True)


#将结果保存到txt
def create_txt(msg):
    path = ".\\static\\resource\\"  # 创建的txt文件的存放路径
    name="识别结果"
    full_path = path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    print(msg)
    print("保存成功")


if __name__ == "__main__":
    app.run(debug=True)