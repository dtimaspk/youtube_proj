from appJar import gui

app = gui("Adicionar Canal")

def add(btn):
	file = open('lista_canais.txt','r')
	urls = file.readlines()
	file.close()
	file = open('lista_canais.txt','w')
	for x in range(len(urls)):
		file.write(urls[x])
	if len(urls) == 0:
		url = app.getEntry('url')
	else:
		url = '\n'+app.getEntry('url')
	file.write(url)
	app.infoBox("Adicionado","O Canal foi adicionado com sucesso!")
	app.clearEntry('url',callFunction = True)
	file.close()

app.setSize(350,30)
app.setResizable(False)
app.setLocation('center')
app.setBg('#272822')

app.addEntry('url',0,0)
app.addButton('Adicionar',add,0,1)

app.go()