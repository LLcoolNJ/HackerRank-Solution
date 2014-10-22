'''C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA
BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC'''

def main():
	p = input()
	lists = ['C','CPP','JAVA','PYTHON','PERL','PHP','RUBY','CSHARP','HASKELL','CLOJURE','BASH','SCALA','ERLANG','CLISP','LUA','BRAINFUCK','JAVASCRIPT','GO','D','OCAML','R','PASCAL','SBCL','DART','GROOVY','OBJECTIVEC']
	w ={}
	oup = []
	t = 'VALID'
	f = 'INVALID'
	for i in range(p):
		w[i] = raw_input()
		w[i] = w[i].split()
		if w[i][1] in lists:
			oup.append(t)
		else:
			oup.append(f)
	for i in oup:
		print i
	
if __name__ == '__main__':
	main() 
