# Makefile
# 
# Purpose: Compile and run unit tests.
# 
# Site: https://dirack.github.io
# 
# Versions 1.0
# 
# Programmer: Rodolfo A C Neves 25/12/2021
# 
# Email: rodolfo_profissional@hotmail.com
# 
# License: GPL-3.0 <https://www.gnu.org/licenses/gpl-3.0.txt>.

# Put your source directory name here (your directory name inside $RFSRC/user)
SRC_DIR :=
# Tests list will be extracted from current folder (Search files with test_*.c pattern)
TESTS := $(patsubst %.c,%.x,$(wildcard test_*.c))
# List your tests dependencies here (No '.c' extension)
DEP_LIST :=

SRC := $(addsuffix .c, $(DEP_LIST))
PACKAGE := $(RSFSRC)/user/$(firstword $(SRC_DIR))
LIB := atestlib
UNITY := Unity/unity.c
GCC := gcc
GCC_OPT := $(UNITY) -I$$RSFSRC/include -I$(PACKAGE) -L. -L$$RSFSRC/lib -lrsf -lm -lblas -l$(LIB)
DEP := $(addprefix $(PACKAGE)/, $(SRC))

# Function to compile and run a test
# The test executable will be removed after running
define RUN_TEST
	$(GCC) $^ $(GCC_OPT) -o $@
	./$@; rm $@
endef

all:	$(TESTS)

# Create a static lib with dependencies
ifdef SRC_DIR
lib$(LIB).a:	$(DEP)
	gcc -c $^ -I$$RSFSRC/include -I$(PACKAGE) -L$$RSFSRC/lib -lm -lrsf
	ar -rc $@ $(patsubst %.c,%.o,$^)
	ranlib $@
else
lib$(LIB).a:
	$(error Variable SRC_DIR is not defined!)
endif

# Rule for running a test
ifndef DEP_LIST
%.x:	%.c
	$(GCC) $^ $(UNITY) -I$$RSFSRC/include -L. -L$$RSFSRC/lib -lrsf -lm -o $@
	./$@; rm $@
else
%.x:	%.c lib$(LIB).a
	$(call RUN_TEST)
endif

clean:
	rm *.x

distclean:
	rm -f *.o *.x lib$(LIB).a

help:
	@echo "Use 'make' to run all the tests"
	@echo "Or run 'make test_filename.x' to run a specific test called filename"
	@echo "Tests available:\n\t$(TESTS)"

.PHONY: distclean clean help
