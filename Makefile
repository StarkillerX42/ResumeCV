
LC=lualatex

all: resume cv autoclean

resume:
	$(LC) dylan_gatlin_cv.tex

cv:
	$(LC) dylan_gatlin_resume.tex

autoclean:
	rm *.aux; rm *.fls; rm *.log; rm *.out; rm *.xdv; rm *latexmk; rm *.synctex.gz

