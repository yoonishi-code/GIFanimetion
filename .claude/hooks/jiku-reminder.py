#!/usr/bin/env python3
"""研究の文章に関わる依頼を検出し、研究の軸の番人（research-compass）による点検を促す。

UserPromptSubmit フックとして動く。標準入力の JSON から prompt を読み、
キーワードに当てはまれば additionalContext として点検の指示を差し込む。
"""
import json
import sys

KEYWORDS = [
    "論文", "研究書", "紀要", "投稿", "査読", "草稿", "原稿",
    "申請", "調書", "科研", "研究計画", "研究設計", "研究テーマ",
    "先行研究", "学会", "発表要旨", "抄録", "研究概要", "業績",
    "授業計画", "シラバス",
]

REMINDER = (
    "【研究の軸の番人】この依頼は研究上の文章に関わる可能性がある。"
    "`.claude/agents/research-compass.md` と `research/profile.md` を基準に、"
    "監視する6項目（①軸への接続 ②言い過ぎ ③判断する主体 ④用語の揺れ "
    "⑤未確認・未読の文献 ⑥二重役割と倫理）と「足りない要点」を点検すること。"
    "文章を書く・直す作業では軸と用語の使い分けに沿って書き、"
    "作業の最後に「いちばん注意すべき一点」と、足りない要点があれば"
    "「この要点が足りません」として短く添えること。"
    "研究の文章に関係のない依頼であれば、この指示は無視してよい。"
)


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return
    prompt = data.get("prompt") or ""
    if prompt.lstrip().startswith("/jiku"):
        return
    if not any(k in prompt for k in KEYWORDS):
        return
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": REMINDER,
        }
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
