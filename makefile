
.PHONY: pubs
pubs:
	git add pubs/\*.*
	make git_add_hili
	git status

git_add_hili:
	git add log/pmids/*.*
	git add log/icite/*.*
	git add log/exports/*.html
	git add log/references/*.txt
	git add src/papers/highlights/*.py
	#git add ms/*.*
	#git add ab/*.*
	# git add src/papers/flashcards/*.py
	#git add doc/papers/\*.pdf
	find log/pubmed -type f | perl -ne 'if ($$_ !~ /p\d+\.txt/) {print}' | xargs git add -f

.PHONY: pap
pap:
	find src/papers/highlights -name \*.py

.PHONY: url
url:
	url.py; cp url url.bib_bac; cp ~/url.bib.today url; vim url

biblog:
	gitlog --re=pubs/bib

bibnot:
	gitlog --re=pubs/notes


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
