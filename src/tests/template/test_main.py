from src.problems.sample.main import main as original_main
from src.tests.sample.main import main as solution_main

"""
正解 or 不正解を判定するためのテストコードを実装しましょう。
作問中は IS_TEST を True に設定（テスト実行時は False に設定）
"""
IS_TEST = True


def test_main():
    result = solution_main() if IS_TEST else original_main()
    assert result == {"message": "Hello, World!"}
