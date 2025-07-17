.PHONY: help

help:
	@echo "利用可能なコマンド:"
	@echo "  create TITLE=[問題のタイトル] - 問題を作成します。"
	@echo "  test TITLE=[問題のタイトル]   - 問題のテストを実行します。"
	@echo "  submit TITLE=[問題のタイトル] - 問題を提出します。"
	@echo "  test.all                     - すべての問題のテストを実行します。"

# 作問者(Questioner) or 解答者(Answerer)
YOUR_STATUS := questioner

create:
	@mkdir -p src/problems/${TITLE}
	@cp -r src/problems/template/* src/problems/${TITLE}/
	@echo "	問題「${TITLE}」のディレクトリを作成しました。"

test:
	@YOUR_STATUS=${YOUR_STATUS} python3 src/problems/${TITLE}/test/test.py

submit:
	@YOUR_STATUS=${YOUR_STATUS} python3 src/problems/${TITLE}/test/test.py

test.all:
	@YOUR_STATUS=${YOUR_STATUS} python3 src/problems/${TITLE}/test/test.py