from functions import Functions
import pandas as pd


if __name__ == '__main__':
    f = Functions()
    f.getPDF()
    if (f.status):        
        d = f.findData()
        colum = [ "No.", "掛號條碼", "收件人", "單位", "收件人簽名", "收件日期"]
        df = pd.DataFrame(d, columns=colum)
        if df.empty: print("好欸!")
        else:
            df.to_excel(f'{f.today}.xlsx', index=False)
            print(df)
            print("excel表做好了ㄛ\n")
    
    print("End ...")