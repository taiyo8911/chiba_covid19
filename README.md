# Python × Streamlitで千葉県コロナ感染者数を可視化

**作成日**：令和3年2月15日
**目的**：千葉県の地域別コロナ感染者数をWeb上で可視化する
**使用ライブラリ**：Python 3、Streamlit、pandas

---

## 概要
Pythonのライブラリ「Streamlit」を使って、千葉県の居住地別感染者数を取得・加工し、Web上で表とグラフとして表示しました。
`main.py` をコンソールで実行すると、ブラウザにWebアプリが立ち上がります。

---

## データ準備
千葉県庁ホームページより「居住地別感染者数」を取得し、CSV形式に加工しました。
**CSVファイル名**：`0215chiba_corona_data.csv`  

| 市町村 | 感染者数 |
|--------|----------|
| 千葉市 | 123      |
| 船橋市 | 87       |
| …      | …        |

---

## Streamlitのインストール
未インストールの場合は、以下を実行：
```bash
pip install streamlit
```

## main.py のコード例
``` python

import streamlit as st
import pandas as pd

# タイトルとサブタイトル
st.title('コロナウイルス千葉県居住地別感染者数')
st.subheader('令和3年2月15日現在')

# CSV読み込み
df = pd.read_csv('0215chiba_corona_data.csv', index_col='市町村')

# 表とグラフ表示
st.dataframe(df)
st.bar_chart(df)

## Webアプリの実行方法
ターミナルまたはコマンドプロンプトで以下を実行：
``` bash
streamlit run main.py
```
ブラウザでWebアプリが立ち上がり、表とグラフを確認できます。


## Streamlitで確認した便利機能
- グラフ上でマウス操作すると詳細情報が表示される
- 表のデータをワンクリックで昇順・降順に並べ替え可能
- わずか数行のコードで、データ系Webアプリが作れることを確認しました。

## 参考情報
- [Pythonで簡単なWebアプリ作成：Streamlitの使い方](https://note.com/maclove/n/n5b95254fa6d3)
- [StreamlitでWebアプリ作成（動画）](https://youtu.be/zp-kAt1Ih5k)


## まとめ（作業メモ）
- Streamlitを使うと、Python初心者でも簡単にWebアプリ化可能
- CSVデータを読み込むだけで、表とグラフ表示ができる
- データ可視化や分析結果の共有に便利
