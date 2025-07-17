"""
コードの正解/不正解を判定するためのコードを記述してください。
"""

import os
import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
if str(parent_dir) not in sys.path:
    sys.path.append(str(parent_dir))

from answer import main as answer_main
from test.solution import main as solution_main

YOUR_STATUS = os.getenv("YOUR_STATUS", "ANSWERER").upper()


def test_main():
    """
    テスト関数
    main関数の出力が期待される形式と一致するかを確認します。
    """

    result = solution_main() if YOUR_STATUS == "ANSWERER" else answer_main()  # noqa: F841

    # 期待される出力を定義
    pass
