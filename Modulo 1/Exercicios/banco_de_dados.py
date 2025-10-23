import sqlite3

con = sqlite3.connect("meu_banco.db")

try:
    con =sqlite3.connect("meu_banco.db")
    cur = con.cursor()
 #   cur.execute("CREATE TABLE pessoa(id, nome, idade, cpf)")
  #  cur.execute("INSERT INTO  pessoa VALUES(1, 'Beatrice', 20, '123.456.789-10')")
    res = cur.execute("SELECT  * FROM  pessoa")
   # cur.execute("DELETE FROM pessoa WHERE id = 1")
   # con.commit()
    #cur.close
    pessoas = res.fetchone()
    print(pessoas)
    con.commit()

except ConnectionRefusedError as c:
    print('Erro de conexão com o banco.')