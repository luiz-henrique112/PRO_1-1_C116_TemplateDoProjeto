# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Lu" # escreva seu nome
    idade = "1,4 décadas" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/painho")
def home2():
    nome = "painho"
    idade = "61"

    return render_template('index.html' , nome = nome , idade = idade)
    
@app.route("/mainha")
def home2():
    nome = "mainha"
    idade = "54"

    return render_template('index.html' , nome = nome , idade = idade)
    
    


# defina a rota para a página da mãe


# defina a rota para a página do amigo


# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
