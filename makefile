

git_add:
	git add pubs/bib/*.bib
	git add pubs/meta/*.yaml
	git add pubs/notes/*.txt
	# git add pubs/doc/*.pdf
	git add log/exports/*.html
	git add log/references/*.txt
	git add src/papers/highlights/*.py
	# git add src/papers/flashcards/*.py
	git add doc/papers/*.pdf
	git status

.PHONY: url
url:
	cp url url.bib_bac; cp ~/url.bib url; vim url

# ----------------------------------------------------------------------
pylint:
	@git status -uno | perl -ne 'if (/(\S+.py)/) {printf "echo $$1\npylint -r no %s\n", $$1}' | tee tmp_pylint
	chmod 755 tmp_pylint
	tmp_pylint

# lists make targets
list:
	@perl -ne 'if (/^([^#.]\S+):/) {print "$$1\n"}' makefile

clean_pyc:
	find . -name \*.pyc | xargs rm -f

clean:
	make clean_pyc
	rm -f tmp_pylint

clean:
	rm -f ex_grades_ecdf.png

# Copyright (C) 2020-present, DV Klopfenstein. All rights reserved.
