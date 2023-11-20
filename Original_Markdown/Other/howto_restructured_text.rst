reStructuredText (RST, ReST, or reST)
=================
is a file format for textual data used primarily in the Python programming language community for technical documentation.  
It is part of the `Docutils <https://docutils.sourceforge.io/>`_ project of the Python Doc-SIG (Documentation Special Interest Group),  
aimed at creating a set  of tools for Python similar to Javadoc for Java or Plain Old Documentation (POD) for Perl. Docutils can  
extract comments and information from Python programs, and format them into various forms of program documentation.  

In this sense, reStructuredText is a lightweight markup language designed to be both processable by documentation-processing  
software such as Docutils, and be easily readable by human programmers who are reading and writing Python source code  

Sphinx
======
Sphinx is a documentation generator or a tool that translates a set of plain text source files into various output formats,  
automatically producing cross-references, indices, etc. That is, if you have a directory containing a bunch of reStructuredText  
or Markdown documents, Sphinx can generate a series of HTML files, a PDF file (via LaTeX), man pages and much more.  

Sphinx focuses on documentation, in particular handwritten documentation, however, Sphinx can also be used to generate blogs,  
homepages and even books. Much of Sphinx’s power comes from the richness of its default plain-text markup format, reStructuredText,  
along with its significant extensibility capabilities.

Sphinx uses the reStructuredText markup language by default, and can read MyST markdown via third-party extensions.  
Both of these are powerful and straightforward to use, and have functionality for complex documentation and publishing workflows.  
They both build upon **Docutils** to parse and write documents.  
`Sphinx Getting Started <https://www.sphinx-doc.org/en/master/index.html>`_  

`Sphinx extended syntax of reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_  


Read the Docs
=============
is an open-sourced free software documentation hosting platform. It generates documentation written with the Sphinx documentation 
generator, MkDocs, or Jupyter Book
`Documentation <https://docs.readthedocs.io/en/stable/index.html>`_
