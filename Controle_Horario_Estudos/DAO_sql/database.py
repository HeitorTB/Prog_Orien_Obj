import sqlite3

class Database:
    conn = None
    nome_bd = "sistema_estudos.db" # Sugestão de nome mais apropriado

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute("PRAGMA foreign_keys = ON") # Importante para o SQLite respeitar as relações

    @classmethod
    def fechar(cls):
        if cls.conn:
            cls.conn.close()

    @classmethod
    def execute(cls, sql, params=None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()
        return cursor

    @classmethod
    def criar_tabelas(cls):
        cls.abrir() # Garante que está aberto antes de criar

        # 1. Tabela Aluno (Antigo Usuário)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            );
        """)

        # 2. Tabela Professor (Nova)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS professor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL,
                formacao TEXT NOT NULL
            );
        """)

        # 3. Tabela Disciplina (Nova - Ligada à Meta)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS disciplina (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                id_professor INTEGER,
                FOREIGN KEY(id_professor) REFERENCES professor(id)
            );
        """)

        # 4. Tabela Meta (Ligada a Disciplina e Aluno)
        # Observação: Adicionei id_aluno para saber de quem é a meta.
        cls.execute("""
            CREATE TABLE IF NOT EXISTS meta (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                data_limite TEXT,
                data_conclusao TEXT,
                status INTEGER DEFAULT 0,
                id_disciplina INTEGER NOT NULL,
                id_aluno INTEGER NOT NULL,
                FOREIGN KEY (id_disciplina) REFERENCES disciplina(id) ON DELETE CASCADE,
                FOREIGN KEY (id_aluno) REFERENCES aluno(id) ON DELETE CASCADE
            );
        """)

        # 5. Tabela Material (Ligada a Professor e Meta)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS material (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                id_professor INTEGER NOT NULL,
                id_meta INTEGER NOT NULL,
                FOREIGN KEY (id_professor) REFERENCES professor(id) ON DELETE CASCADE,
                FOREIGN KEY (id_meta) REFERENCES meta(id) ON DELETE CASCADE
            );
        """)

        # 6. Tabela HorarioEstudo (Ligada a Aluno e Meta)
        # Baseado no diagrama, o horário conecta o aluno a uma meta de estudo
        cls.execute("""
            CREATE TABLE IF NOT EXISTS horario_estudo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_hora_inicio TEXT NOT NULL,
                data_hora_fim TEXT NOT NULL,
                id_aluno INTEGER NOT NULL,
                id_meta INTEGER NOT NULL,
                FOREIGN KEY (id_aluno) REFERENCES aluno(id) ON DELETE CASCADE,
                FOREIGN KEY (id_meta) REFERENCES meta(id) ON DELETE CASCADE
            );
        """)

        print("Tabelas criadas/verificadas com sucesso!")
        cls.fechar()

if __name__ == "__main__":
    Database.criar_tabelas()

if __name__ == "__main__":
    Database.abrir()
    Database.criar_tabelas()
    print(f"Banco de dados '{Database.nome_bd}' e tabelas criados com sucesso!")
    Database.fechar()