"""
コードの正解/不正解を判定するためのコードを記述してください。
"""

import io
import json
import os
import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
if str(parent_dir) not in sys.path:
    sys.path.append(str(parent_dir))

from answer import main as answer_main
from solution import main as solution_main

YOUR_STATUS = os.getenv("YOUR_STATUS", "ANSWERER").upper()


def test_main():
    """
    テスト関数
    main関数の出力が期待される形式と一致するかを確認します。
    """
    # テストケースをtestcases.jsonから読み込む
    with open(str(parent_dir / "test/testcases.json"), "r") as f:
        testcases = json.load(f)

    for case in testcases:
        # 標準入力をモック
        stdin = sys.stdin
        sys.stdin = io.StringIO(case["input"])
        # 標準出力をキャプチャ
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            if YOUR_STATUS == "ANSWERER":
                answer_main()
            else:
                solution_main()
            output = sys.stdout.getvalue().strip()
        finally:
            sys.stdin = stdin
            sys.stdout = stdout
        # 出力の正誤判定
        if output != case["output"].strip():
            print(f"[INFO] 想定解：{case['output']}, 受け取った値：{output}")
            return 1
    return 0


if __name__ == "__main__":
    flg = test_main()
    if YOUR_STATUS == "ANSWERER":
        if flg:
            print(" ❌ 残念！！")
            sys.exit(flg)
        else:
            print(" ⭕️ 正解！！")
    else:
        if flg:
            print(" ❌ テストに失敗しました。")
            sys.exit(flg)
        else:
            print(" ✅ テストが成功しました！！")
