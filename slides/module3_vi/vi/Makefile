# Copy this into each set of notes. 
# It lets us update the preamble and the Makefile

TEMPLATE_URL := https://github.com/mikewojnowicz/latex_preamble

update-preamble:
	git clone $(TEMPLATE_URL) .latex_preamble
	# 
	cp ".latex_preamble/preamble.sty" .
	# 
	rm -rf .latex_preamble
	@echo "Updated preamble.sty updated. Don't forget to commit."

update-makefile:
	git clone $(TEMPLATE_URL) .latex_preamble
	# 
	cp ".latex_preamble/Makefile" .
	# 
	rm -rf .latex_preamble
	@echo "Updated preamble.sty updated. Don't forget to commit."
