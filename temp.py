import pandas as pd
import os
wsi_path_list1 = pd.read_excel(r"\\shelter\Kyu\skin_aging\clue_cohort\CLUE_image_list_230207_v2.xlsx", engine='openpyxl')
wsi_path_list2 = wsi_path_list1[(wsi_path_list1['student score'] > 1)]
wsi_path_list3 = wsi_path_list2.set_index('index')
wsi_path_list4 = wsi_path_list3.sort_index()
wsi_path_list = [os.path.join(r'\\shelter\Kyu\skin_aging\clue_cohort\wsi', _) for _ in wsi_path_list4['filename'].tolist()]
print(wsi_path_list)