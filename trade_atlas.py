
import pandas as pd

url_base_less99 = 'https://www.tradeatlas.com/en/hs-code-categories/silicon-containing-by-weight-less-than-9999-of-silicon?hs-code=280469&page={}'
url_base_high99='https://www.tradeatlas.com/en/hs-code-categories/silicon-containing-by-weight-less-than-9999-of-silicon?hs-code=280461&page={}'
result_dfs = []

for i in range(1,56):
    url = url_base_high99.format(i)
    web = pd.read_html(url)
    data = pd.DataFrame(web[0])
    result_dfs.append(data)
    print(str(i)+'. page has done...!')

result_df = pd.concat(result_dfs, ignore_index=True)

with pd.ExcelWriter('output2.xlsx') as writer:
    result_df.to_excel(writer, index=False)
