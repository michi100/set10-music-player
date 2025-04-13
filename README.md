### 絵や音楽を編集する

`cd assets` \
`pyxel edit`

### watch モードで起動

`cd set10-music-player` \
`pyxel watch game game/main`

- update 関数はフレーム更新処理を行う
- draw 関数は描画処理を行う

### html ファイル作成

`cd set10-music-player` \
`pyxel package .\game\ .\game\main.py` .pyxelapp ファイルが生成される\
`cd web`\
`pyxel app2html ..\game.pyxapp` web フォルダの中に.html ファイルが生成される \
`mv .\game.html ..\public\` \
`cd set10-music-player` \
`firebase deploy --only hosting`

上記は Windows11 で実施した手順。
