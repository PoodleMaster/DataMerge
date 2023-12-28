# DataMerge
data_20231201.csv
```
Serial,DeviceName,Count
AAA1,1-1WiFi,10
BBB1,1-2WiFi,20
CCC1,1-3WiFi,30
```

data_20231202.csv
```
Serial,DeviceName,Count
AAA1,1-1WiFi,15
BBB1,1-2WiFi,25
CCC1,1-3WiFi,35
```

data_20231203.csv
```
Serial,DeviceName,Count
AAA1,1-1WiFi,19
BBB1,1-2WiFi,29
CCC1,1-3WiFi,39
```

# Exec
```
python ./merge.py
結合が完了し、ファイルが ./merge.tsv に保存されました。
```

```
python ./merge.py --output-format csv
結合が完了し、ファイルが ./merge.csv に保存されました。
```

```
python ./merge.py --output-format tsv
結合が完了し、ファイルが ./merge.tsv に保存されました。
```

# Result
merge.tsv
```tsv
Serial	DeviceName	2023/12/01	2023/12/02	2023/12/03
AAA1	1-1WiFi	10	15	19
BBB1	1-2WiFi	20	25	29
CCC1	1-3WiFi	30	35	39
```

merge.csv
```csv
Serial,DeviceName,2023/12/01,2023/12/02,2023/12/03
AAA1,1-1WiFi,10,15,19
BBB1,1-2WiFi,20,25,29
CCC1,1-3WiFi,30,35,39
```
