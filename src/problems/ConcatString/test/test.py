"""
コードの正解/不正解を判定するためのコードを記述してください。
"""

import json
import os
import sys
from io import StringIO
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
        input_args = case["input"]
        stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            if YOUR_STATUS == "ANSWERER":
                answer_main(*input_args)
            else:
                solution_main(*input_args)
            output = sys.stdout.getvalue().strip()
        finally:
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
