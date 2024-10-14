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

# 参考
* [InfluxDB+Grafana構築 on docker #Docker - Qiita]( https://qiita.com/7280ayubihs/items/ace07b14d934dca4744c )
* [GrafanaとInfluxDBで作るProxmoxダッシュボード【Docker】 | Konsome Engineering]( https://engineering.konso.me/articles/make-proxmox-dashboard-using-grafana-and-influxdb/ )
