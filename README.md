# rt-dashboard

``` bash
docker compose up -d
```

## influxdb
http://localhost:8086/

> DOCKER_INFLUXDB_INIT_USERNAME=admin 
> DOCKER_INFLUXDB_INIT_PASSWORD=password 

## grafana
http://localhost:8085/

* Email or username: admin
* > GF_SECURITY_ADMIN_PASSWORD=admin 

## sample
``` bash
pip install influxdb-client
pip install python-dotenv
```

# How to use
## Grafana
### InfluxDBのデータソースを登録する
左メニュー > `Connections` >  `Data sources` > `Add data source`

`influxdb`を選択する

* `Query language`: `Flux`を選択すること(`InfluxQL`では正常に認証ができなかった)
* HTTP
  * URL: `http://influxdb-local:8086`
* Auth
  * `User`: `admin`
  * `Password`: `password`
* InfluxDB Details
  * Organization: `organization`
  * Token: プログラム用に生成して、`.env`で使用しているトークンか新しく生成したトークンを利用すること
  * Default Bucket: `bucket`

`Save & test`をクリックする

### データソースをダッシュボードに表示させる
``` bash
./data-sender.py
```
を実行しながら次のステップを踏む

右上の`+`から`New dashboard`
`Add visualization`から`InfluxDB`のデータソースを選択する

`Query`
```
from(bucket: "bucket")
|> range(start: -5m)
```
を入力して、上部パネルの`♻️`ボタンを押して更新するとデータが表示される

この作成したパネルを配置したダッシュボードを保存すること

ダッシュボード上でリアルタイムにデータが反映されるようにするには上部のパネルから自動更新を`Auto`にすると5秒間隔でデータが更新されるようになった

![sample screenshot]( https://private-user-images.githubusercontent.com/21164287/376147003-fae3198e-950a-40e7-8b10-ae6f6923eaf5.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjg4OTI0NDgsIm5iZiI6MTcyODg5MjE0OCwicGF0aCI6Ii8yMTE2NDI4Ny8zNzYxNDcwMDMtZmFlMzE5OGUtOTUwYS00MGU3LThiMTAtYWU2ZjY5MjNlYWY1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDE0VDA3NDkwOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdhYjMzNTQ3YTAzYjQxYTVjNmU2NzI3YjQ2NWQ5NDNhZjk1ODAzZWRiMjZmZWU3NmVhOGQxODEyMGFkOTUxZjMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.XYX8hv1NKpIeTqT35HykvQpkXvTUwS5VyrQwf1kV1PM )

# NOTE
* DBからのデータ取得やそのデータソースの可視化のスパンを考えると1秒単位のリアルタイムは難しく、10秒単位のリアルタイムが限界なのではないか?
* ちょっとした可視化に対してはオーバースペックである

# 参考
* [InfluxDB+Grafana構築 on docker #Docker - Qiita]( https://qiita.com/7280ayubihs/items/ace07b14d934dca4744c )
* [GrafanaとInfluxDBで作るProxmoxダッシュボード【Docker】 | Konsome Engineering]( https://engineering.konso.me/articles/make-proxmox-dashboard-using-grafana-and-influxdb/ )
