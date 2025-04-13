### 絵や音楽を編集する

`cd assets` \
`pyxel edit`

### watch モードで起動

`cd set10-music-player` \
`pyxel watch game game/main`

- update 関数はフレーム更新処理を行う
- draw 関数は描画処理を行う

### html ファイル作成、デプロイ

`cd set10-music-player` \
`pyxel package .\game\ .\game\main.py` game.pyxapp ファイルを生成する\
`pyxel app2html game.pyxapp` game.pyxapp から game.html ファイルを生成する \
`mv .\game.html .\public\index.html` html ファイルを public フォルダに移動 \
`firebase deploy --only hosting`

上記は Windows11 で実施した手順。
