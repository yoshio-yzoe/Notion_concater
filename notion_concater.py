import glob
import os
from bs4 import BeautifulSoup


def merge_html(input_dir: str = 'input_data', output_file: str = 'merged.html') -> None:
    # 新規ドキュメントを lxml パーサで生成
    merged = BeautifulSoup(
        '<!DOCTYPE html><html><head></head><body></body></html>',
        'lxml'
    )
    merged_head = merged.head
    merged_body = merged.body

    # head タグの重複排除用セット
    seen_head = set()

    # ファイル名順にマージ
    paths = sorted(glob.glob(os.path.join(input_dir, '*.html')))
    for html_path in paths:
        with open(html_path, encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'lxml')

        # head 以下の meta/link/style/script を一度だけマージ
        for tag in soup.head.find_all(['meta', 'link', 'style', 'script'], recursive=False):
            key = (tag.name, tuple(sorted(tag.attrs.items())))
            if key not in seen_head:
                seen_head.add(key)
                merged_head.append(tag)

        # body の直下要素（<article> + コメントの<span>等）をまとめてマージ
        section = merged.new_tag('section', **{'data-source': os.path.basename(html_path)})
        for child in soup.body.find_all(recursive=False):
            section.append(child)
        merged_body.append(section)

    # 出力ファイル書き出し
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(merged.prettify(formatter='html'))

    print(f"Merged {len(paths)} files into {output_file}")


if __name__ == '__main__':
    # デフォルト設定で実行
    merge_html()