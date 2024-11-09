# Jogo da forca
# Desenvolvido por: Miguel Vieira
# Desenvolvido em 23/10/2024

# Importação da biblioteca random que fornece funções para gerar números e seleções aleatórias
import random
from flask import Flask, session, request, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'meuJogo'

# Dicionário de palavras e suas respectivas pistas
palavras_pistas = {
     'python': 'A programming language known for its simplicity and readability, used in many fields such as data science and automation',
    'html': 'A markup language used to structure pages on the web',
    'php': 'A programming language used on servers for dynamic website development',
    'javascript': 'A programming language essential for adding interactivity to web pages',
    'java': 'A widely used language in corporate software development and mobile applications',
    'sql': 'A language used to manage and manipulate relational databases',
    'css': 'A styling language used to control the layout and appearance of web pages',
    'ruby': 'A programming language focused on simplicity and productivity, used in frameworks',
    'pascal': 'A classical programming language often used for teaching programming',
    'c': 'One of the oldest and most efficient programming languages, still widely used for operating systems and low-level software'
}

# Função para iniciar o jogo e armazenar valores na sessão
def iniciar_jogo():
    palavra, pista = random.choice(list(palavras_pistas.items()))  # Escolha de um par de palavra e pista aleatório
    session['palavra'] = palavra
    session['pista'] = pista
    session['chances'] = 3
    session['tracejado'] = ['_'] * len(palavra)
    session['letras_tentadas'] = []

# Rota para a página inicial e iniciar o jogo
@app.route('/')
def index():
    iniciar_jogo()
    return redirect(url_for('jogar'))

# Rota para jogar
@app.route('/jogar', methods=['GET', 'POST'])
def jogar():
    if 'palavra' not in session:
        iniciar_jogo()  # Inicia o jogo se a palavra não estiver na sessão

    mensagem = ''  # Inicializa a variável mensagem
    mensagem_correta = ''  # Inicializa a variável mensagem_correta

    if request.method == 'POST':
        # Tentar adivinhar a palavra inteira
        if 'palavra_inteira' in request.form and request.form['palavra_inteira'].strip():
            palavra_inteira = request.form['palavra_inteira'].lower().strip()

            if palavra_inteira == session['palavra']:
                return render_template('resultado.html', mensagem='Congratulations, you guessed the word!', palavra=session['palavra'])
            else:
                session['chances'] -= 1
                mensagem = 'Incorrect word. Try again.'

        # Tentar adivinhar uma letra
        elif 'letra' in request.form and request.form['letra'].strip():
            letra = request.form['letra'].lower().strip()  # Transformar a letra em minúscula e armazenar na variável

            # Verificar se a entrada é válida (uma única letra)
            if not letra.isalpha() or len(letra) != 1:
                mensagem = 'Please enter a valid letter.'
            # Verificar se a letra tentada já foi inserida
            elif letra in session['letras_tentadas']:
                mensagem = "You've already tried that letter. Try a different one!"
            else:
                session['letras_tentadas'].append(letra)  # Adiciona a letra tentada ao final da lista
                # Atualizar o progresso do jogador
                if letra in session['palavra']:
                    tracejado_atualizado = session['tracejado']  # Atualiza a lista tracejado sem recarregar o progresso
                    for i, char in enumerate(session['palavra']):
                        if char == letra:
                            session['tracejado'][i] = letra  # Atualiza as letras no tracejado da posição correta
                    session['tracejado'] = tracejado_atualizado
                    mensagem_correta = 'Good job! You guessed a letter correctly.'
                else:
                    session['chances'] -= 1
                    mensagem = 'Incorrect letter. Try again.'

        # Se as chances acabaram
        if session['chances'] <= 0:
            return render_template('resultado.html', mensagem='You lost!', palavra=session['palavra'])
        elif '_' not in session['tracejado']:  # Jogador ganhou (todas as letras foram adivinhadas)
            return render_template('resultado.html', mensagem='Congratulations, you guessed it!', palavra=session['palavra'])

    # Primeira renderização ou após cada tentativa
    return render_template('jogar.html', 
                           pista=session['pista'], 
                           tracejado=' '.join(session['tracejado']),
                           chances=session['chances'], 
                           letras_tentadas=session['letras_tentadas'], 
                           mensagem=mensagem,
                           mensagem_correta=mensagem_correta)

# Executar a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)