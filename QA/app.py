from flask import Flask, render_template, request

app = Flask(__name__ )
@app.route("/", methods=['GET', 'POST'])
def index():
    context = ''
    if request.method == 'POST':
        question = request.form.get('question') if request.form.get('question') is not None else ""
        print(question)
        if len(question) > 0:
            answer = query_process(question)#gerar frase de consulta
            respost = similaridade_sentencas(answer)

            # coloca o processamento da rede aq
            context = respost
    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
