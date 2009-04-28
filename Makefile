# Makefile for Pynq
SHELL := /bin/bash

# Internal variables.
file_version=0.1.0
root_dir=.
build_dir=${root_dir}/build
src_dir=${root_dir}/pynq

tests_dir=${root_dir}/tests
unit_tests_dir=${tests_dir}/unit
functional_tests_dir=${tests_dir}/functional

compile_log_file=${build_dir}/compile.log
unit_log_file=${build_dir}/unit.log
functional_log_file=${build_dir}/functional.log

nocoverage=false

help:
	@echo
	@echo "    Pynq Makefile v${file_version}"
	@echo "    usage: make <target>"
	@echo
	@echo "    targets:"
	@echo "    help             displays this help text"
	@echo "    all              compiles the code and runs all tests"
	@echo "    clean            cleans the build directory"
	@echo "    compile          compiles the python code"
	@echo "    test             runs all tests (unit and functional)"
	@echo "    unit             runs all unit tests"
	@echo "    functional       runs all functional tests"
	@echo "    codeanalyis      generates code analysis info"
	@echo

# orchestrator targets

unit: prepare_build compile run_unit report_success
functional: prepare_build compile run_functional report_success

all: prepare_build compile test report_success

prepare_build: clean create_build_dir

test: run_unit run_functional

clean: remove_build_dir

# action targets

report_success:
	@echo "Build succeeded!"

remove_build_dir:
	@rm -fr ${build_dir}

create_build_dir:
	@mkdir -p ${build_dir}

compile:
	@echo "Compiling source code..."
	@rm -f ${compile_log_file} >> /dev/null
	@rm -f -r ${src_dir}/*.pyc >> /dev/null
	@python -m compileall ${src_dir} >> ${compile_log_file} 2>> ${compile_log_file}

run_unit: compile
	@echo "Running unit tests..."
	@rm -f ${unit_log_file} >> /dev/null
	@if [ "$(nocoverage)" = "true" ]; then nosetests --verbose ${unit_tests_dir} >> ${unit_log_file} 2>> ${unit_log_file}; else nosetests --verbose --with-coverage --cover-package=pynq ${unit_tests_dir} >> ${unit_log_file} 2>> ${unit_log_file}; fi
	@echo "============="
	@echo "Unit coverage"
	@echo "============="
	@if [ "$(nocoverage)" != "true" ]; then cat ${unit_log_file} | egrep '(Name)|(TOTAL)'; fi
	@if [ "$(nocoverage)" = "true" ]; then echo 'Coverage Disabled.'; fi
	@echo
	
run_functional: compile
	@echo "Running functional tests..."
	@rm -f ${functional_log_file} >> /dev/null
	@if [ "$(nocoverage)" = "true" ]; then nosetests --verbose ${functional_tests_dir} >> ${functional_log_file} 2>> ${functional_log_file}; else nosetests --verbose --with-coverage --cover-package=pynq ${functional_tests_dir} >> ${functional_log_file} 2>> ${functional_log_file}; fi
	@echo "==================="
	@echo "Functional coverage"
	@echo "==================="
	@if [ "$(nocoverage)" != "true" ]; then cat ${functional_log_file} | egrep '(Name)|(TOTAL)'; fi
	@if [ "$(nocoverage)" = "true" ]; then echo 'Coverage Disabled.'; fi
	@echo
	
codeanalyis:
	@echo "Generating code analysis..."
	@sloccount ${root_dir}
	
