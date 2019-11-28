all:
	mkdir -p build
	./py-puml-tools/py2puml/py2puml.py -r src/ --recursive src/__init__.py > build/project.uml
	rm py2puml.log
	plantuml build/project.uml
	doxygen
