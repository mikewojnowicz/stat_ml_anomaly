# We use Make to encapsulate many of
# the shell commands for managing our projects. Each project
# has a `Makefile` and a `Makefile_gen.mk`. `Makefile_gen.mk` is a
# "canonical" file that should not be modified from what is
# defined in the template. If make fails to find a
# target in `Makefile`, it will fall back on the default
# commands in `Makefile_gen.mk`. Any given target in
# `Makefile_gen.mk` can be overridden in `Makefile`. In addition,
# you can define arbitrary, project-specific targets here.


##########################################
### Required Variables ###################
##########################################
NAME := anomaly
VERSION := $(shell cat VERSION)
SOURCES := $(shell find src -name '*.py')
TARBALL := dist/$(NAME)-$(VERSION).tar.gz

##########################################
### Project Specific Targets #############
##########################################

# Check your code for style, run your unit tests, and make a package
all: lint test test-integration clean-build build

## Example: Custom `clean` target to remove pyc files
## Note that this overrides the default `clean` behavior
## defined in `Makefile_ds.mk`.
#
# clean: clean-tarballs
# 	rm -rf *.pyc
#

# Override the pre-commit file; we don't use that here.
# Install all dependencies from requirements files
env: requirements.txt dev-requirements.txt
# Tox doesn't automatically recreate an environment if requirements change
	tox -vv -e env --notest --recreate
	if [ -d ".git" ]; then tox -vv -e env -- install; fi
# Tox's operations may not update the modified time on the env folder, so unless
# we do that ourselves, make will constantly rebuild this target after either of
# the requirements files have been changed.
	@touch env

##########################################
### REQUIRED TARGETS: DO NOT DELETE ######
##########################################

# The code below is required to fall back on the
# canonical Makefile defined in `Makefile_gen.mk`.
export NAME VERSION SOURCES TARBALL
%: force
	@$(MAKE) --makefile Makefile_gen.mk $@
force: ;
.PHONY: Makefile all
