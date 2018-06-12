.PHONY: all prepare testJsonLdJs

all:
	echo No default target.

prepare:
	sudo apt-get update ;\
		sudo apt-get upgrade -y ;\
		sudo n stable ;\
		sudo npm install -g jsonld cross-env mocha chai join-path-js fs-extra semver rdf-canonize request

testJsonLdJs:
	cd jsonld.js; \
		npm install --save-dev chai join-path-js fs-extra semver rdf-canonize request; \
	 	npm run fetch-test-suites; \
		npm test


