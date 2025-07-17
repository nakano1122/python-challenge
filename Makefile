.PHONY: help

help:
	@echo "利用可能なコマンド:"
	@echo "  create_problem TITLE=[問題のタイトル] - 問題を作成します。"
	@echo "  test_problem TITLE=[問題のタイトル]   - 問題のテストを実行します。"
	@echo "  submit_problem TITLE=[問題のタイトル] - 問題を提出します。"

create_problem:
	@echo "問題「{TITLE}」を作成します。"
	@python3

test_problem:
	@echo "問題「{TITLE}」のテストを実行します。"
	@python3

test_all:
	@echo "すべての問題のテストを実行します。"
	@python3

submit_problem:
	@echo "問題「{TITLE}」を提出します。"
	@python3
