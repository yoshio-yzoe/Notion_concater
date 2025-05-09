# Notion Concater

複数の Notion からエクスポートした HTMLファイル（コメント含む）を情報欠落なく結合し、単一の HTML を生成するスクリプトです。

## 📋 ディレクトリ構成

```text
notion_concater/
├── notion_concater.py      # 結合スクリプト本体
├── input_data/             # Notion からエクスポートした HTML ファイルを格納するディレクトリ
│   ├── page1.html
│   ├── page2.html
│   └── …
└── README.md
```

## 🔧 Notion からの HTML エクスポート手順

1. 結合したい親ページを Notion で開く。
2. 右上のメニュー（•••）から **"Export"** を選択。
3. **フォーマット** を **HTML** に設定。
4. **対象コンテンツ** を **すべて** にする。
5. **サブページを含める** を **ON** にする。
6. **サブページのフォルダーを作成** を **OFF** にする。
7. **コメントをエクスポート** を **ON** にする。
8. **Export** をクリックし、ZIP をダウンロード。
9. ダウンロードした ZIP を解凍し、生成されたフォルダ内のすべての `.html` ファイルを `input_data/` フォルダにコピー。

   * サブページ用のフォルダ構造は作成せず、すべて平置きしてください。
   * 例: `Exported/page-a.html`, `Exported/SubPage B.html` → `input_data/page-a.html`, `input_data/SubPage B.html`

## 🛠 環境構築（Conda）


```bash
conda create -n notion_concater python=3.11
conda activate notion_concater
conda install -c conda-forge beautifulsoup4 lxml
```

## 🚀 スクリプト実行方法

```bash
# デフォルト動作
python notion_concater.py
# 実行後、スクリプトと同階層に merged.html が生成されます。
```
