# PyUML

* Supposedly supports UML -> Python code generation.
* Cannot be installed automatically: PyUML requires PyDev 1.x.x while PyDev is currently at 7.4.0
* Upon closer inspection: PyUML has not been updated since 2013
* Type hints were introduced with Python 3.5, which was released in 2015. It is therefore imposible for PyUML to support type hints.
* It would be a huge pain in the ass to set up an old version of Eclipse with an old version of Pydev (which we would have to compile ourselves). I think this extra work pretty much cancels out with the advantage of being able to generate stubs.
