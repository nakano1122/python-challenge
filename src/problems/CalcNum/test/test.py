"""
コードの正解/不正解を判定するためのコードを記述してください。
"""

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
    with open(parent_dir / "test/testcases.json", "r") as f:
        test_cases = json.load(f)
    
    input_data = [case["input"] for case in test_cases]
    expected_outputs = [case["output"] for case in test_cases]

    for input_case, expected_output in zip(input_data, expected_outputs):
        a, b = input_case
        result = (
            answer_main(a, b)
            if YOUR_STATUS == "ANSWERER"
            else solution_main(a, b)
        )

        # 出力の正誤判定
        if result != expected_output:
            print(f"[INFO] 想定解：{expected_output}, 受け取った値：{result}")
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
