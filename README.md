# FastAPI_Dynamodb

### AWS CLI をインストール
```
インストール
  brew install awscli

バージョン確認
  aws --version
```

### AWS CLI の設定
```
aws configure

下記の入力を求められるので、アクセスキーやリージョンを記載
↓
AWS Access Key ID: 
AWS Secret Access Key: 
Default region name: 
Default output format: 


(参考)
AWS Access Key ID: IAMユーザー作成後に作成できる
AWS Secret Access Key: IAMユーザー作成後に作成できる
Default region name: ap-northeast-1
Default output format: json
```

### ビルドとデプロイ
```
ソース変更したらビルド
  sam build

デプロイ
  sam deplpy

デプロイ設定を変更したい場合
　sam deploy --guided
```

### エンドポイント確認方法 下記２パターン
- ⓵ sam list endpoints --stack-name [samconfig.tomlのstack_name]
- ⓶ AWS マネジメントコンソール（API Gatewayのステージ）で確認

### 各種ファイル説明
- template.yaml：インフラ構築するテンプレート

- samconfig.toml：デプロイ設定のテンプレート

  　これがあると ```sam deplpy``` のみでok
