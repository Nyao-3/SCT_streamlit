import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("SCT results")

    # サイドバーにファイルのアップロードを設置
    uploaded_file = st.sidebar.file_uploader("① CSVファイルをアップロードしてください", type="csv")
    
    # サイドバーにID選択のための入力ボックスを設置
    id_input = st.sidebar.text_input("② 表示させたいIDを入力してください")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        # 入力されたIDがデータフレームに存在するか確認し、該当する行を表示
        if not id_input:
            st.write("IDを入力してください")
        else:
            id_input = int(id_input)
            selected_row = data[data['ID'] == id_input]
            if selected_row.empty:
                st.subheader("該当するIDが見つかりません")
            else:
                if pd.isnull(selected_row['age'].values[0]):
                    st.subheader("該当するIDが見つかりません")
                else:
                    st.subheader(f"{int(selected_row['age'].values[0])}歳（成人用）")

            # 選択したIDのすべての行についてループ処理
            for i, row in selected_row.iterrows():
                
                st.divider()

                selected_row_emotions_values = selected_row[["Joy", "Trust", "Fear", "Surprise", "Sadness", "Disgust", "Anger", "Anticipation"]]
                selected_row_emotions = pd.DataFrame(selected_row_emotions_values.values, columns=selected_row_emotions_values.columns, index=["Emotional Intensity"])
                st.dataframe(selected_row_emotions)
                
                st.write("Note: The Emotional Intensity is commonly rated on a 9-point scale, with anchor points set at 0 for 'none', 2 for 'mild', 4 for 'moderate', 6 for 'strong', and 8 for 'extreme'.")

                st.header("身体的要因")
                st.write(str(row["Physical_F"]))

                st.header("家庭的要因")
                st.write(str(row["Domestic_F"]))

                st.header("社会的要因")
                st.write(str(row["Social_F"]))

                st.divider()

                # "側面＞スキーム"の下に特定の列のテキストを表示
                st.subheader("環境＞社会")
                st.write("P1_01: " + str(row["P1_01"]))
                st.write("P1_13: " + str(row["P1_13"]))
                st.write("P1_18: " + str(row["P1_18"]))
                st.write("P1_20: " + str(row["P1_20"]))
                st.write("P1_26: " + str(row["P1_26"]))
                st.write("P1_29: " + str(row["P1_29"]))
                st.write("P2_03: " + str(row["P2_03"]))
                st.write("P2_08: " + str(row["P2_08"]))
                st.write("P2_10: " + str(row["P2_10"]))
                st.write("P2_11: " + str(row["P2_11"]))
                st.write("P2_16: " + str(row["P2_16"]))

                st.subheader("環境＞家庭")
                st.write("P1_03: " + str(row["P1_03"]))
                st.write("P1_05: " + str(row["P1_05"]))
                st.write("P1_09: " + str(row["P1_09"]))
                st.write("P1_17: " + str(row["P1_17"]))
                st.write("P1_21: " + str(row["P1_21"]))
                st.write("P1_25: " + str(row["P1_25"]))
                st.write("P2_01: " + str(row["P2_01"]))
                st.write("P2_06: " + str(row["P2_06"]))
                st.write("P2_12: " + str(row["P2_12"]))
                st.write("P2_18: " + str(row["P2_18"]))
                st.write("P2_23: " + str(row["P2_23"]))
                st.write("P2_26: " + str(row["P2_26"]))

                st.subheader("身体")
                st.write("P1_15: " + str(row["P1_15"]))
                st.write("P1_27: " + str(row["P1_27"]))
                st.write("P2_09: " + str(row["P2_09"]))
                st.write("P2_20: " + str(row["P2_20"]))

                st.subheader("能力")
                st.write("P1_14: " + str(row["P1_14"]))
                st.write("P2_15: " + str(row["P2_15"]))

                st.subheader("性格＞気質")
                st.write("P1_02: " + str(row["P1_02"]))
                st.write("P1_22: " + str(row["P1_22"]))
                st.write("P2_04: " + str(row["P2_04"]))
                st.write("P2_22: " + str(row["P2_22"]))

                st.subheader("性格＞力動")
                st.write("P1_04: " + str(row["P1_04"]))
                st.write("P1_06: " + str(row["P1_06"]))
                st.write("P1_07: " + str(row["P1_07"]))
                st.write("P1_24: " + str(row["P1_24"]))
                st.write("P1_30: " + str(row["P1_30"]))
                st.write("P2_02: " + str(row["P2_02"]))
                st.write("P2_19: " + str(row["P2_19"]))
                st.write("P2_21: " + str(row["P2_21"]))
                st.write("P2_24: " + str(row["P2_24"]))
                st.write("P2_25: " + str(row["P2_25"]))
                st.write("P2_30: " + str(row["P2_30"]))

                st.subheader("指向")
                st.write("P1_08: " + str(row["P1_08"]))
                st.write("P1_10: " + str(row["P1_10"]))
                st.write("P1_11: " + str(row["P1_11"]))
                st.write("P1_12: " + str(row["P1_12"]))
                st.write("P1_16: " + str(row["P1_16"]))
                st.write("P1_19: " + str(row["P1_19"]))
                st.write("P1_23: " + str(row["P1_23"]))
                st.write("P1_28: " + str(row["P1_28"]))
                st.write("P2_05: " + str(row["P2_05"]))
                st.write("P2_07: " + str(row["P2_07"]))
                st.write("P2_13: " + str(row["P2_13"]))
                st.write("P2_14: " + str(row["P2_14"]))
                st.write("P2_17: " + str(row["P2_17"]))
                st.write("P2_27: " + str(row["P2_27"]))
                st.write("P2_28: " + str(row["P2_28"]))
                st.write("P2_29: " + str(row["P2_29"]))

if __name__ == "__main__":
    main()