from cefpython3 import cefpython as cef
import sys
import win32gui
import get_info as g_i
import html_builder as builder

def main():
	sys.excepthook = cef.ExceptHook
	cef.Initialize()
	#MUDAR A URL PARA O CAMINHO ONDE SE ENCONTRA ESTE FICHEIRO
	cef.CreateBrowserSync(url = 'file:///C:/Users/Utilisador/Desktop/projects/youtube_proj/main_window.html',
		window_title = 'youtube_proj')
	win = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(win,500,25,350,700,True)
	cef.MessageLoop()
	cef.Shutdown()

def get_urls():
	file = open('lista_canais.txt','r')
	urls = file.readlines()
	file.close()
	return urls

def get_lista_canais():
	urls = get_urls()
	str_ = ''
	for x in range(len(urls)):
		str_ += g_i.get_info_canal(urls[x],x+1)
		print('--------------------------------------------')
	return str_

def get_lista_videos():
	urls = get_urls()
	str_ = ''
	for x in range(len(urls)):
		str_ += g_i.get_info_video(urls[x],x+1)
		print('--------------------------------------------')
	return str_

str_canais=get_lista_canais()
str_videos=get_lista_videos()
str_script=builder.criar_javascript(len(get_urls()))
builder.criar_html(str_canais,str_videos,str_script)

main()