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

# Put your source directory name here (your directory name inside $RFSRC/user)
SRC_DIR := 
# List the main programs here (No 'M' or 'sf' preffix nor extension)
PROGRAMS_LIST := 
# List your programs dependencies here (No '.c' extension)
DEP_LIST := 

SRC := $(firstword $(RSFSRC)/user/$(SRC_DIR))
DEP := $(addsuffix .c, $(addprefix $(SRC)/,$(DEP_LIST)))
PROGRAMS := $(addsuffix .gdbx, $(PROGRAMS_LIST))
LIB := adebuglib

all:	$(PROGRAMS)

# functions to call gdb scripts
include makefile_plugins/gdb_runners

# functions to generate a new gdb script
include makefile_plugins/new_gdb_runner

# GNU debugger (GDB) runners
%.debug:	%.gdbx gdb_scripts/run_console gdb_scripts/$(script)
ifdef	script
	$(call RUN_CONSOLE,$(script),$<)
else
	$(call RUN_CONSOLE,run_console,$<)
endif

%.hacker:	%.gdbx gdb_scripts/run_console gdb_scripts/$(script)
ifdef	script
	$(call HACKER,$(script),$<)
else
	$(call HACKER,run_console,$<)
endif

# Build program versions for GNU debugger (GDB)
ifndef DEP
%.gdbx:	$(SRC)/M%.c
	gcc -fbounds-check -DGDB_DEBUG -g $^ -I$$RSFSRC/include -I.. -L. -L$$RSFSRC/lib -o $@ -lrsf -lm -lblas
else
%.gdbx:	$(SRC)/M%.c lib$(LIB).a
	gcc -fbounds-check -DGDB_DEBUG -g $^ -I$(SRC) -I$$RSFSRC/include -I.. -L. -L$$RSFSRC/lib -o $@ -lrsf -lm -lblas
endif

# Create a static lib with dependencies
lib$(LIB).a:    $(DEP)
	gcc -c $^ -I$$RSFSRC/include -I$(SRC) -L$$RSFSRC/lib -lm -lrsf
	ar -rc $@ $(patsubst %.c,%.o,$^)
	ranlib $@

clean:
	rm *.gdbx

distclean:
	rm *.gdbx *.o *.a

help:
	@echo "Use 'make' to compile all GDB programs versions"
	@echo "Use 'make progname.gdbx' to generate a version of progname for debug with GDB"
	@echo "Use 'make progname.debug' to generate a version of progname for GDB and start console"
	@echo "Use 'make progname.debug script=gdb_script' to generate a version of progname for GDB, start console and load gdb_script in it"
	@echo "Programs available:"
	@echo "\t$(PROGRAMS_LIST)"
	@echo "Sources directory:"
	@echo "\t$(SRC)"
	@echo "Dependencies:"
	@echo "\t$(notdir $(DEP))"

.PHONY: clean distclean help
