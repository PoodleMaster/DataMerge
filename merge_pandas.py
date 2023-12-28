import os
import pandas as pd
from datetime import datetime
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Merge CSV or TSV files with specified date format.')
    parser.add_argument('--output-format', choices=['csv', 'tsv'], default='csv', help='Output file format (csv or tsv)')
    return parser.parse_args()

def main():
    args = parse_args()

    # 出力ファイルの拡張子と区切り文字を設定
    if args.output_format == 'csv':
        output_ext = 'csv'
        delimiter = ','
    elif args.output_format == 'tsv':
        output_ext = 'tsv'
        delimiter = '\t'
    else:
        raise ValueError("Invalid output format. Use 'csv' or 'tsv'.")

    # データが格納されているディレクトリ
    input_dir_path = './csv_data/'

    # ファイル名から日付を抽出して、ソート
    file_list = sorted([f for f in os.listdir(input_dir_path) if f.endswith(".csv")], key=lambda x: x.split('_')[1].split('.')[0] if '_' in x else '')

    # 空の辞書を作成して、SerialとDeviceNameをキーにしてデータを格納
    all_data_dict = {}

    # 日付を保持するリスト
    dates = []

    # ディレクトリ内の各CSVファイルをソートされた順で処理
    for filename in file_list:
        file_path = os.path.join(input_dir_path, filename)

        # CSVファイルを読み込み
        df = pd.read_csv(file_path, header=0)  # ヘッダーを指定
        date_str = filename.split('_')[1].split('.')[0] if '_' in filename else ''
        date = datetime.strptime(date_str, "%Y%m%d").strftime("%Y/%m/%d")
        dates.append(date)

        # SerialとDeviceNameをキーにしてデータを格納
        for _, row in df.iterrows():
            key = (row['Serial'], row['DeviceName'])  # カラム名を指定

            if key not in all_data_dict:
                all_data_dict[key] = {'Serial': key[0], 'DeviceName': key[1]}

            all_data_dict[key][date] = row['Count']

    # 結果を新しいファイルに保存
    output_file_path = f'./merge.{output_ext}'

    # DataFrameを生成
    df_result = pd.DataFrame.from_dict(all_data_dict, orient='index', columns=['Serial', 'DeviceName'] + sorted(set(dates)))

    # ヘッダーを指定してCSVファイルに書き込む
    df_result.to_csv(output_file_path, sep=delimiter, index=False, header=True, mode='w')

    # 結果の表示
    print('結合結果:')
    print(df_result)

    print(f'結合が完了し、ファイルが {output_file_path} に保存されました。')

if __name__ == '__main__':
    main()
