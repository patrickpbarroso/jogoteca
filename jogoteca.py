from flask import Flask, render_template

class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console
    
    def __str__(self):
        return self.nome
    
    @property
    def get_caracteristicas_jogo(self):
        return f'{self.nome} | {self.categoria} | {self.console}'

app = Flask(__name__)

@app.route('/home')
def home():
    jogo1 = Jogo('Genshin Impact', 'RPG de mundo aberto', 'PC/Playstation/Mobile')
    jogo2 = Jogo('League of Legends', 'MOBA', 'PC')
    jogo3 = Jogo('Pokemon Soul Silver', 'RPG', 'Nintendo DS')
    jogo4 = Jogo('Fortnite', 'Battle Royale', 'PC')

    lista_de_jogos = [jogo1, jogo2, jogo3, jogo4]
    return render_template('lista.html', titulo='Jogos', jogos=lista_de_jogos)

app.run()