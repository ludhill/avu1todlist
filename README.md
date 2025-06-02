Testar manualmente
1. Ativar o ambiente virtual
source venv/bin/activate  # Linux/macOS
.venv\Scripts\activate  # Windows

2. Inicializar o banco de dados
flask --app flaskr init-db

3. Executar a aplicação
flask --app flaskr run --debug

4. Testar manualmente
Acesse as rotas principais da aplicação no navegador:

/auth/register → Teste o cadastro de usuários.

/auth/login → Teste o login.

/todo/create → Teste a criação de tarefas.

/todo/ → Veja se as tarefas.

5. Testar automaticamente
pip install pytest
pytest
