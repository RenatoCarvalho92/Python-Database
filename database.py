import psycopg2
import psycopg2.extras
from psycopg2 import sql
from flask import Flask, request


hostname = 'localhost'
database = 'postgres'
nomeUsuario = 'postgres'
senha = 'admin'
portId = '5432'

teste1 =4
teste2='Ronaldo'
teste3='ronaldo@email'
teste4="1234"

variavel_nome_calendario = "nomeCalendario11"

app = Flask(__name__)




@app.route('/teste')
def testando(): 
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = nomeUsuario,
            password = senha,
            port =portId)

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute ('DROP TABLE IF EXISTS empressa')

    script_criar = '''CREATE TABLE IF NOT EXISTS empressa (
                    id int PRIMARY KEY,
                    nomeempressa varchar(360) NOT NULL,
                    emailempressa varchar(360) NOT NULL,
                    senha varchar(360) NOT NULL)'''

    script_inserir ='INSERT INTO empressa (id, nomeEmpressa, emailempressa, senha) VALUES (%s,%s,%s,%s)'
    script_valores = (teste1,teste2,teste3,"123456")

    cur.execute(script_criar)
    cur.execute(script_inserir,script_valores)


    # cur.execute('SELECT *  FROM EMPRESSA WHERE ID = 4')
    # for record in cur.fetchall():
    #     print(record['emailempressa'],record['senha'])
    
    cur.execute(f'SELECT *  FROM EMPRESSA WHERE ID = {teste1}') #Verificar email se existe no banco de dados
    x= cur.fetchone()
    if x == None: 
        print ("Vazio") #Voltar para pagina porque não encontrou algo ou algo está errado
    else:               #SENÃO , vai para verificar se a senha recebida está correta 
        if teste4 == x[3]: 
            print("Tudo Correto") #Vai para proxima pagina 
        else:
            print("Senha Errada") #Volta a pagina anterior// mensagaem para tentar novamente
        
        
    conn.commit()

    conn.close()
    return "Teste Completo"



@app.route('/')
def criarTabelaCalendario():
    
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = nomeUsuario,
            password = senha,
            port =portId)

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    
    
    cur.execute (f'''DROP TABLE IF EXISTS {variavel_nome_calendario}''')
    script_tabela_calendario = f'''CREATE TABLE IF NOT EXISTS  {variavel_nome_calendario}
                    (dia_mes_ano VARCHAR(8) NOT NULL,
                     email_empressa VARCHAR NOT NULL,
                     nota_Dia VARCHAR NOT NULL)'''
                     
    # script_tabela_calendario_valores = "Teste"
    
    cur.execute(script_tabela_calendario)
    
    conn.commit()

    conn.close()
    
    return "Tabela criada com sucesso"


@app.route('/AdicionarDia',methods=["POST"])
def AddDia():
    json_data = request.get_json()
    
    nome_tabela_dia = json_data['nome_tabela_dia']
    dia_aser_adicionado = "1"
    email_da_empressa = 2
    nota_do_dia = "3"
    
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = nomeUsuario,
            password = senha,
            port =portId)
    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    script_adicionar_dia = f'''INSERT INTO {nome_tabela_dia} (dia_mes_ano,email_empressa,nota_dia) 
                            VALUES ({dia_aser_adicionado},{dia_aser_adicionado},{nota_do_dia})'''
    
    # script_adicionar_dia = f'''INSERT INTO {nome_tabela_dia} (dia_mes_ano,email_empressa,nota_dia) 
    #                         VALUES ({[dia_aser_adicionado,dia_aser_adicionado,nota_do_dia]})'''
    
    # script_adicionar_dia =sql.SQL ("INSERT INTO %s (dia_mes_ano,email_empressa,nota_dia) VALUES (%s,%s,%s)")
    # teste_var = [nome_tabela_dia,dia_aser_adicionado,email_da_empressa,nota_do_dia]
    
    # cur.execute(script_adicionar_dia,teste_var,)
    
    # script_adicionar_dia = 'INSERT INTO {} (dia_mes_ano,email_empressa,nota_dia) VALUES ({},{},{})'.format(nome_tabela_dia,dia_aser_adicionado,email_da_empressa,nota_do_dia)
    
    # script_adicionar_dia = "INSERT INTO " + nome_tabela_dia + " (dia_mes_ano,email_empressa,nota_dia) VALUES ("+dia_aser_adicionado+","+email_da_empressa+","+nota_do_dia+")"
    
    # script_adicionar_dia = "INSERT INTO %s (dia_mes_ano,email_empressa,nota_dia) VALUES (%s,%s,%s)"
    # script_adicionar_dia_value = (nome_tabela_dia,dia_aser_adicionado,email_da_empressa,nota_do_dia)
    
    # cur.execute("INSERT INTO %s (dia_mes_ano,email_empressa,nota_dia) VALUES (%s,%s,%s);",(nome_tabela_dia,dia_aser_adicionado,email_da_empressa,nota_do_dia))
    
    # script_adicionar_dia = """INSERT INTO %s (dia_mes_ano,email_empressa,nota_dia) VALUES (%s,%s,%s)"""
    # script_adicionar_dia_value = (json_data['nome_tabela_dia'],dia_aser_adicionado,email_da_empressa,nota_do_dia)
    
    
    
    # cur.execute(script_adicionar_dia,script_adicionar_dia_value)
    

    cur.execute(script_adicionar_dia)
    
    # cur.execute(sql.SQL("INSERT INTO {table} (dia_mes_ano,email_empressa,nota_dia) VALUES (%s,%s,%s)").format(table = sql.Identifier("nomecalendario11")),(nome_tabela_dia,dia_aser_adicionado,email_da_empressa,nota_do_dia,))
    
    
    
    
    
    conn.commit()
    conn.close()
    return {}, 200

app.run()