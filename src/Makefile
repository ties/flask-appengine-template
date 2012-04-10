#
#
#
COMPILED_TEMPLATES = compiled_templates.zip
REVISION_FILE = ./application/templates/revision.html

jinja2_templates = $(shell find application -name templates -type d -exec find {} \;)

branch_name := $(shell git symbolic-ref -q HEAD)
ifeq ($(branch_name), )
	branch = "(unnamed branch)"
else
	branch := $(notdir $(branch_name))
endif

revision := $(shell git describe --always)

${REVISION_FILE}:
	echo "${branch} - $(revision)" > ${REVISION_FILE}
	

${COMPILED_TEMPLATES}: $(jinja2_templates)
	python prepare_templates.py

all: ${REVISION_FILE} ${COMPILED_TEMPLATES}
	
clean:
	rm -f ${REVISION_FILE}
	rm -f ${COMPILED_TEMPLATES}

.PHONY: all