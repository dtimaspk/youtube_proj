
html = ''

html_pre = """
	<!DOCTYPE html>
	<html>
	<head>
		<title></title>
	</head>
	<body>
		<div id="lista_canal">
"""
html_meio = """ 
	</div>
		<div id="lista_video">
"""
html_fim_pre = """
		</div>
		<style type="text/css">
			body{
				background-color: #272822;
			}
			#lista_canal{
				float: left;
			}
			#lista_video{
				float: right;
				border-left: solid 1px red;

			}
			.canal{
				width: 50px;
				height: 50px;
				margin: 10px;
				padding: 1px;
			}
			.canal img{
				width: 50px;
			}
			.video{
				width: 192px;
				height: 170px;
				margin: 10px;
				padding: 5px;
			}
			.video img{
				width: 192px;
				height: 108px;
			}
			h4, a{
				padding: 0px;
				margin: 0px;
				text-decoration: none;
				font-family: Arial, Helvetica, sans-serif;
				color: white;
			}
		</style>
		<script type="text/javascript" src="jquery.js"></script>
		<script type="text/javascript">
"""
html_fim_fim = """
	</script>
	</body>
	</html>
"""
def criar_div_canal(str_img, num):
	div_pre = '<div id="id_canal_'+str(num)+'" class="canal"><img src='
	div_fim = '></div>'
	img_src = '"'+str_img+'"'
	div = div_pre+img_src+div_fim
	return div

def criar_div_video(str_img, str_titulo, str_link, num):
	div_pre = '<div class="video video_'+str(num)+'"><a target="_blank" href="'+str_link+'"><img src='
	div_fim = '><h4>'+str_titulo+'</h4></a></div>'
	img_src = '"'+str_img+'"'
	div = div_pre+img_src+div_fim
	return div

def criar_javascript(num):
	script_pre = '$(document).ready(function(){'
	script_hide = ''
	script_click = ''
	script_hover = ''
	for x in range(num-1):
		script_hide += '$(".video_'+str(x+2)+'").hide();'
	for x in range(num):
		script_click += '$("#id_canal_'+str(x+1)+'").click(function(){'
		for z in range(num):
			if x == z:
				script_click += '$(".video_'+str(z+1)+'").show();'
				script_click += 'document.getElementById("id_canal_'+str(z+1)+'").style.border = "solid 2px red";'
			else:
				script_click += '$(".video_'+str(z+1)+'").hide();'
				script_click += 'document.getElementById("id_canal_'+str(z+1)+'").style.border = "solid 0px red";'
		script_click += '});'
	for x in range(num):
		script_hover += """$('#id_canal_"""+str(x+1)+"""').hover(function() {
		$('#id_canal_"""+str(x+1)+"""').css({ transform: 'scale(1.15)' });
		});$('#id_canal_"""+str(x+1)+"""').mouseout(function() {
			$('#id_canal_"""+str(x+1)+"""').css({ transform: 'scale(1)' });
		});"""

		
	script = script_pre+script_hide+script_click+script_hover+'});'
	return script


def criar_html(str_canais, str_videos, str_script):
	html = html_pre+str_canais+html_meio+str_videos+html_fim_pre+str_script+html_fim_fim
	file = open('main_window.html','w')
	file.write(html)