# Define the documents to be constructed and the desired file types
DOCUMENTS= dissertation \
		   defense

OUTPUTS=$(addsuffix .pdf,$(DOCUMENTS))
all: $(OUTPUTS)

# Build rawfigs/*.eps into figs/*.pdf
FIGS_EPS=$(patsubst rawfigs/%,figs/%,$(patsubst %.eps,%.pdf,$(wildcard rawfigs/*.eps)))
$(FIGS_EPS) : figs/%.pdf : rawfigs/%.eps ; epstopdf --outfile=$@ $<
FIGURES += $(FIGS_EPS)

# Build rawfigs/*.pdf into figs/
FIGS_PDF=$(patsubst rawfigs/%,figs/%,$(wildcard rawfigs/*.pdf))
$(FIGS_PDF) : figs/%.pdf : rawfigs/%.pdf ; cp $< $@
FIGURES += $(FIGS_PDF)

# Build rawfigs/*.png into figs/
FIGS_PNG=$(patsubst rawfigs/%,figs/%,$(wildcard rawfigs/*.png))
$(FIGS_PNG) : figs/%.png : rawfigs/%.png ; cp $< $@
FIGURES += $(FIGS_PNG)

# Build rawfigs/*.jpg into figs/
FIGS_JPG=$(patsubst rawfigs/%,figs/%,$(wildcard rawfigs/*.jpg))
$(FIGS_JPG) : figs/%.jpg : rawfigs/%.jpg ; cp $< $@
FIGURES += $(FIGS_JPG)

# Build rawfigs/*.ps into figs/
FIGS_PS =$(patsubst rawfigs/%,figs/%,$(patsubst %.ps, %.eps,$(wildcard rawfigs/*.ps)))
$(FIGS_PS)  : figs/%.pdf : rawfigs/%.ps  ; ps2pdf $< $@
FIGURES += $(FIGS_PS)

# Build rawfigs/*.svg into figs/
FIGS_SVG=$(patsubst rawfigs/%,figs/%,$(patsubst %.svg,%.pdf,$(wildcard rawfigs/*.svg)))
$(FIGS_SVG) : figs/%.pdf : rawfigs/%.svg ; env --unset=DISPLAY inkscape -z $< --export-pdf=$@ --export-dpi=300
FIGURES += $(FIGS_SVG)

# Ensure figs/ exists before using it, clean up figs/, and build figures before docs
$(FIGURES): | figs-directory-mkdir
clean:      | figs-directory-rm
figs-directory-mkdir: ; @mkdir -p figs
figs-directory-rm:    ; @rm -rf figs
$(addsuffix .pdf,$(DOCUMENTS)) : $(FIGURES)

# Use latexmk to build PDFs directly
.PRECIOUS : %.pdf
LATEXMK?=latexmk
%.pdf : %.tex FORCE ;    $(LATEXMK) -dvi- -ps- -pdf "-deps-out=$*.dep" $< \
                      || $(LATEXMK) -dvi- -ps- -pdf                    $<

# Use inotifywait to re-run 'make all' whenever any input changes
# Depends on a newer latexmk version supporting the -deps-out option
# The grep -v 'INPUT ' portion of the pipeline discards broken filenames in *.dep
continuous: all ; bash -c "while true; do inotifywait -e close_write -e delete_self -e move --fromfile <(grep -h '^[[:blank:]]' *.dep | grep -v 'INPUT \|OUTPUT ' | sed -e 's/^[[:blank:]]*//' -e 's/\\\$\//'| sort -u) || break; $(MAKE) all; done"

clean : FORCE
	@for o in $(OUTPUTS); do $(LATEXMK) -quiet -f -C $$o & done ; wait
	@rm -f $(addsuffix .out,$(DOCUMENTS)) $(addsuffix .dep,$(DOCUMENTS))
	@rm -f *.aux *.aux.bak *.bbl *.nav *.snm *.tdo

FORCE : # http://www.gnu.org/software/make/manual/html_node/Force-Targets.html
