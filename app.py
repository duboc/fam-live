from flask import Flask, render_template
import random

app = Flask(__name__)

jokes = [
    {
        "setup": "Por que o esqueleto não brigou com ninguém?",
        "punchline": "Porque ele não tinha estômago para isso!"
    },
    {
        "setup": "O que o pato disse para a pata?",
        "punchline": "Vem Quá!"
    },
    {
        "setup": "Qual é o cúmulo da sorte?",
        "punchline": "Ser atropelado por uma ambulância."
    },
    {
        "setup": "Por que a galinha atravessou a rua?",
        "punchline": "Para chegar ao outro lado."
    },
    {
        "setup": "O que um programador diz quando se afoga?",
        "punchline": "Log, log, log..."
    }
]

@app.route('/')
def home():
    selected_joke = random.choice(jokes)
    return render_template('index.html', joke_setup=selected_joke['setup'], joke_punchline=selected_joke['punchline'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
