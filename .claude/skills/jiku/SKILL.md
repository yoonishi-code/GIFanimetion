---
name: jiku
description: 研究の軸の番人（research-compass）を呼び出し、論文・申請書・研究設計などの草稿が研究の軸からずれていないかを点検する。/jiku の後に、草稿のファイル名や点検したい内容を書いて使う。
---

これから、`.claude/agents/research-compass.md` に定義された「研究の軸の番人」として草稿を点検してください。

1. `.claude/agents/research-compass.md` と `research/profile.md` を読み、そこに書かれた軸・点検の観点・応答の形式に従う。
2. ユーザーが草稿（ファイル、Google Drive の文書、貼り付けた文章）を示していれば、それを読んでから点検する。示されていなければ、何を点検するかを短く尋ねる。
3. 応答は「いちばん注意すべき一点」から始める。

点検の対象: $ARGUMENTS
