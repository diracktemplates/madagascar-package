# Makefile
# 
# Purpose: Compile GDB programs versions and run then in debug mode in GDB.
# 
# Site: https://www.geofisicando.com
# 
# Version 1.0
# 
# Programmer: Rodolfo A C Neves (Dirack) 05/10/2020
# 
# Email: rodolfo_profissional@hotmail.com
# 
# License: GPL-3.0 <https://www.gnu.org/licenses/gpl-3.0.txt>.

DEP :=
SRC := .
PACKAGE :=
PROGRAMS :=
LIB := adebuglib

all:	$(PROGRAMS)

# functions to call gdb scripts
include makefile_plugins/gdb_runners

# GNU debugger (GDB) runners
%.debug:	$(SRC)/%.gdbx gdb_scripts/run_console gdb_scripts/$(script)
ifdef	script
	$(call RUN_CONSOLE,$(script),$<)
else
	$(call RUN_CONSOLE,run_console,$<)
endif

%.hacker:	$(SRC)/%.gdbx gdb_scripts/run_console gdb_scripts/$(script)
ifdef	script
	$(call HACKER,$(script),$<)
else
	$(call HACKER,run_console,$<)
endif

# Build program versions for GNU debugger (GDB)
ifndef DEP
%.gdbx:	$(SRC)/%.c
	gcc -fbounds-check -DGDB_DEBUG -g $^ -I$$RSFSRC/include -I.. -L$$RSFSRC/lib -o $@ -lrsf -lm
else
%.gdbx:	$(SRC)/%.c lib$(LIB).a
	gcc -fbounds-check -DGDB_DEBUG -g $^ -I$$RSFSRC/include -I.. -L$$RSFSRC/lib -o $@ -lrsf -lm
endif

# Create a static lib with dependencies
lib$(LIB).a:    $(DEP)
	gcc -c $^ -I$$RSFSRC/include -I$$RSFSRC/user/$(PACKAGE) -L$$RSFSRC/lib -lm -lrsf
	ar -rc $@ $(patsubst %.c,%.o,$^)
	ranlib $@

clean:
	rm *.gdbx

help:
	@echo "Use 'make' to compile all GDB programs versions"
	@echo "Use 'make progname.gdbx' to generate a version of progname for debug with GDB"
	@echo "Use 'make progname.debug' to generate a version of progname for GDB and start console"
	@echo "Use 'make progname.debug script=gdb_script' to generate a version of progname for GDB, start console and load gdb_script in it"
	@echo "Programs available:"
	@echo "$(PROGRAMS)"
	@echo "Sources directory:"
	@echo "$(SRC)"
	@echo "Dependencies:"
	@echo "$(DEP)"

.PHONY: clean help
