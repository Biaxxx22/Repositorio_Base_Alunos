filmes={
    "drama": ["Ainda Estou Aqui","O Poderoso Chefão", "Ela"],
    "comédia": ["Tempos Modernos","American Pie","Dr. Dolittle"],
    "policial": ["O Exterminador do Futuro","O Procurado","Velozes e Furiosos"],
    "guerra": ["Rambo","1917","Até o Último Homem"],
    "ação": ["Tropa de elite","Infiltrado"],
    "terror":["Corra","Invocação do mal"],
    "doramas":["Pousando no amor","Sorriso real","All of Us Are Dead","Pretendente surpresa","My Demon"],
    "animes":["Evangelion", "One Piece","Dragon ball","JoJo's","Haikyuu"],
    "Drama":["Grey's anatomy","Tomboy","The mirror","Magnolia","O jardim secreto"]
    
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