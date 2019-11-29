all:
	mkdir -p build
	./py-puml-tools/py2puml/py2puml.py -r src/ --recursive src/__init__.py > build/project.puml
	rm py2puml.log
	plantuml config.puml -o build
	doxygen
	make --directory=./build/latex
