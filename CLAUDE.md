# このリポジトリについて

研究者・大西洋（北海道教育大学岩見沢校／視覚伝達デザイン）の研究支援用の設定を置いている。

- `research/profile.md`：研究紹介、研究の軸（制作を翻訳として捉える立場）、用語の使い分け、参照文献
- `.claude/agents/research-compass.md`：研究の軸の番人（`/jiku` で呼び出す）
- `.claude/agents/aesthetics-scholar.md`：美学研究の第一人者のペルソナ（`/bigaku` で呼び出す）

## 研究上の文章を扱うときの原則

論文・申請書・研究設計・授業計画などを書いたり直したりするときは、依頼が明示されていなくても `research/profile.md` の軸と用語の使い分けに沿って書く。軸からのずれ、データに比べた言い過ぎ、未確認の文献に気づいたら、作業の最後に一言添える。

## 自動点検（フック）

`.claude/settings.json` の UserPromptSubmit フック（`.claude/hooks/jiku-reminder.py`）が、メッセージに「論文」「申請」「調書」「草稿」「研究計画」などの言葉を含むとき、research-compass の基準で点検するよう指示を差し込む。キーワードはスクリプト内の `KEYWORDS` で増減できる。
