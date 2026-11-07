.PHONY: all build compare check reading-copy
all: build compare check
build:
	python3 build.py
compare:
	python3 compare/dump_sat.py && python3 compare/build_cmp.py
check: build
	node tools/check-layout.js && node tools/check-goals.js
reading-copy: build
	node tools/reading-copy.js
