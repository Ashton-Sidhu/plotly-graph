.PHONY: tests

tests:
	poetry run pytest

tags:
	git commit --allow-empty -m "Release $(rel)"
	git push upstream --tags
	git tag -a $(rel) -m "Version $(rel)"
