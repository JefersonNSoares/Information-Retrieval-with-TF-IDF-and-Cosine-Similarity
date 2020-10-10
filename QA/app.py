from flask import Flask, render_template, request

app = Flask(__name__ , static_url_path='/static')
@app.route("/", methods=['GET'])
def index():
    context = ''
    question = request.args.get('question') if request.args.get('question') is not None else ""
    if len(question) > 0:
        answer = "resposta"
        # coloca o processamento da rede aq
        context = answer
    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
