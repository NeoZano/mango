import re ,os

def render(filename,var):
	file = open("web/"+filename, "r").read()
	for norse_tag in re.findall(r'(?<={{).*?(?=}})', file):

			# include tag
			if "include" == norse_tag.split()[0]:
				file = file.replace("{{"+norse_tag+"}}", open("web/"+norse_tag.split()[1].replace("'",""),"r").read())
			# var tag or error
			else:
				text_inside_tag = str(os.path.splitext(norse_tag)[0]).replace(" ","")
				try:
					var[text_inside_tag]
				except KeyError:
					print("[error] : var '"+text_inside_tag+"' does'nt exist")
				else:
					file = file.replace("{{"+norse_tag+"}}", str(var[text_inside_tag]))
	return file
