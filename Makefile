.PHONY: help

help:
	@echo "利用可能なコマンド:"
	@echo "  create TITLE=[問題のタイトル] - 問題を作成します。"
	@echo "  test TITLE=[問題のタイトル]   - 問題のテストを実行します。"
	@echo "  submit TITLE=[問題のタイトル] - 問題を提出します。"
	@echo "  test.all                     - すべての問題のテストを実行します。"

# 作問者(Questioner) or 解答者(Answerer)
YOUR_STATUS := Answerer

create:
	@mkdir -p src/problems/${TITLE}
	@cp -r src/problems/_template/* src/problems/${TITLE}/
	@echo "	問題「${TITLE}」のディレクトリを作成しました。"

test:
	if [ "$(YOUR_STATUS)" = "Answerer" ]; then \
		echo "❌ エラー: 解答者はsubmitできません。"; \
		exit 1; \
	fi
	@YOUR_STATUS=${YOUR_STATUS} python3 src/problems/${TITLE}/test/test.py

submit:
	if [ -z "${TITLE}" ]; then \
		echo "❌ エラー: TITLEを指定してください。"; \
		exit 1; \
	fi
	@YOUR_STATUS=${YOUR_STATUS} python3 src/problems/${TITLE}/test/test.py

test.all:
	if [ "$(YOUR_STATUS)" = "Answerer" ]; then \
		echo "❌ エラー: 解答者はsubmitできません。"; \
		exit 1; \
	fi
	@YOUR_STATUS=${YOUR_STATUS} python3 src/problems/${TITLE}/test/test.py
