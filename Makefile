SHELL := /bin/zsh

.PHONY: help check build preview push

help:  ## Show this help
	@grep -E '^[a-z-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-10s %s\n", $$1, $$2}'

check:  ## Dashes gate (must pass before build)
	sh scripts/check-dashes.sh

build: check  ## Build figures + deck + preview
	uv run python scripts/render.py all

preview:  ## Regenerate PNG previews only
	uv run python scripts/render.py preview

push:  ## Push to both remotes
	git push github main
	git push gitlab main
