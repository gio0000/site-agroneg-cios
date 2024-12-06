from flask import Flask, flash, render_template, request, redirect, session, url_for
import mysql.connector

# Configuração do aplicativo Flask
app = Flask(__name__)
app.secret_key = 'chave_secreta_segura'  # Troque por uma chave segura

# Configuração do banco de dados MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'agro'
}

# Testando conexão com o banco de dados
def connect_db():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Conexão com o banco de dados bem-sucedida!")
        return connection
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


# Página inicial
@app.route('/')
def index():
    usuario = session.get('usuario')  # Obtém o nome do usuário, se logado
    return render_template('index.html', usuario=usuario)


# Modelos de equipamentos
@app.route('/equipamentos')
def equipamentos():
    return render_template('equipamentos.html')


# Notícias do setor
@app.route('/noticias')
def noticias():
    return render_template('noticias.html')


# Página sobre a empresa
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']

        conn = connect_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT usuario, senha FROM usuario WHERE usuario = %s AND senha = %s", (usuario, senha))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['usuario'] = user['usuario']
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciais inválidas. Tente novamente.', 'danger')

    return render_template('tela_de_login.html')


# Cadastro de usuários
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        usuario = request.form['nome']
        senha = request.form['senha']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuario (usuario, senha) VALUES (%s, %s)', (usuario, senha))
        conn.commit()
        conn.close()

        flash('Cadastro realizado com sucesso! Faça login.', 'success')
        return redirect(url_for('login'))

    return render_template('cadastro.html')


# Logout
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
