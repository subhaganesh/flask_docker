from flask import Flask, request,render_template

app = Flask(__name__)

@app.route('/',methods=['get'])
def home():
    return 'welcome to the marks cacluating page'

@app.route('/calculate', methods=['post'])
def calculate_marks():
    marks = []
    for i in range(1, 6):
        subject_mark = int(request.form[f'mark{i}'])
        marks.append(subject_mark)
    
    total_marks = sum(marks)
    
    result = "Pass" if total_marks > 50 else "Fail"
    
    return result

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)


