import os
import csv
from datetime import datetime
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Merge CSV or TSV files with specified date format.')
    parser.add_argument('--output-format', choices=['csv', 'tsv'], default='tsv', help='Output file format (csv or tsv)')
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
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)

            # ファイル名から日付を抽出
            date_str = filename.split('_')[1].split('.')[0] if '_' in filename else ''
            date = datetime.strptime(date_str, "%Y%m%d").strftime("%Y/%m/%d")

            # 日付をリストに追加
            dates.append(date)

            # SerialとDeviceNameをキーにしてデータを格納
            for row in reader:
                key = (row[0], row[1])

                if key not in all_data_dict:
                    all_data_dict[key] = {}

                all_data_dict[key][date] = row[2]

    # 結果を新しいファイルに保存
    output_file_path = f'./merge.{output_ext}'
    with open(output_file_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file, delimiter=delimiter)

        # ヘッダーを書き込む
        writer.writerow(['Serial', 'DeviceName'] + sorted(set(dates)))

        # データを書き込む
        for key, date_values in all_data_dict.items():
            values = [date_values.get(date, '') for date in sorted(dates)]
            writer.writerow(list(key) + values)

    print(f'結合が完了し、ファイルが {output_file_path} に保存されました。')

if __name__ == '__main__':
    main()
