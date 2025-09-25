filmes={
    "drama": ["Ainda Estou Aqui","O Poderoso Chefão", "Ela","A viagem","O jardim secreto"],
    "comédia": ["Tempos Modernos","American Pie","Dr. Dolittle","Barbie","Anos 90"],
    "policial": ["O Exterminador do Futuro","O Procurado","Velozes e Furiosos","Infiltrado","Anonimo"],
    "guerra": ["Rambo","1917","Até o Último Homem","Munique","Rambo"],
    "ação": ["Tropa de elite","Infiltrado","Matrix","Batman","Missão impossível"],
    "terror":["Medo profundo","Invocação do mal","Annabelle","Corra","Panico"],
    "doramas":["Pousando no amor","Sorriso real","All of Us Are Dead","Pretendente surpresa","My Demon"],
    "animes":["Evangelion", "One Piece","Dragon ball","JoJo's","Haikyuu"],
    "fantasia":["Narnia","O Hobbit","O senhor dos aneis","O sétimo filho","O magico de Oz"],
    "romance":["Sr. & Sra. Smith","Os agentes do destino","Amor de aluguel","A Bela e a Fera","Aladdin"]
    
    
}
página=open("filmes.html","w", encoding="utf-8")
página.write("""
<!DOCTYPE html>
    <html lang="pt-BR">
        <head>
        <meta charset="utf-8">
        <title>Filmes</title>
        </head>
        <body> 
""")
for c, v in filmes.items():
    página.write("<h1>%s</h1>" % c)
    for e in v:
        página.write("<h2>%s</h2>" % e)
página.write("""
</body>
</html>
""")
página.close()