# 作問者向けドキュメント

## 問題追加手順

`Makefile`の`YOUR_STATUS`の値を`ANSWER`にしてください。

1. `make create TITLE=<問題名>`コマンドを実行して、問題テンプレートフォルダを作成します。

2. テストコードは `test/test.py` に記述し、`main()` の出力が期待値と一致するか判定してください。

3. 模範解答は`test/solution.py`に記述し、`make test TITLE=<問題名>`コマンドを実行して正誤判定が正常に動作するか確認してください。

## テストの書き方
- `test/test.py` で `from answer import main as answer_main` で解答をインポートします。
- `from test.solution import main as solution_main` で模範解答をインポートします。
- `assert` 文で出力の正誤判定を行います。

## 問題を作る際の注意点

- 問題名はなるべく分かりやすくしてください。（パスカルケースでの定義を推奨）
- 問題文は答えが一意に定まるように設定してください。
- 処理の正誤判定を行うために、テストケースを積極的に作りましょう。

## ディレクトリ構成例
```
src/problems/sample/
├── answer.py
├── test/
│   ├── solution.py
│   └── test.py
```
