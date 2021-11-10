# slack-pin-scheduler

をつくりたい

## 一回読んだ

* [Djangoの環境をDocker化する（Docker + Django + Gunicorn + nginx）その１ - Qiita](https://qiita.com/amazipangu/items/bce228f506f894cd825d)
* [ローカルにあるdocker-composeプロジェクトをリモートのDockerで実行する - Qiita](https://qiita.com/legacyworld/items/0fb8507a8951e13f8061)
* [docker-composeでpostgresの設定を変更する方法 - Qiita](https://qiita.com/ihatov08/items/72bb5bd4feeef87e77a5)

一番最初のものを中心に進めてきたが、微妙にうまく行ってないので方針検討中

## 今考えていること
### bata版

![bata版](./docs/image/slack-scheduler-bata.png)

メモリに持たせて再起動ごとに壊れてしまうものの、一旦この形にしてみる

### alpha版

![alpha版](./docs/image/slack-scheduler-alpha.png)

postgresを活用したい。
