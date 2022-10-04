.PHONY: tests

version := $$(awk '/version/ {print $$3}' pyproject.toml | tr -d \")

tests:
	poetry run pytest

tags:
	git tag -a ${version} -m 'Update version'
	git push origin ${version}

release:
	gh release create ${version} --generate-notes
