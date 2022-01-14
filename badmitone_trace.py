####algo#####
        #print(box)
        if (box[0]>970 or box[0]<930)and (box[1]>=290) :
            all_list[0].append(box[0])
            all_list[1].append(box[1])
        try:
            if y_list[-2]>=290 and y_list[-1]>=290:
                #all_list = [x_list,y_list]
                df = pd.DataFrame(all_list)
                df=df.T
                df.columns=["x","y"]
                df1 = df.copy()
                inx=df1[df1.x == 0].index
                df1= df1.drop(inx)
                df1.reset_index(inplace=True,drop=True)
                df2=df1.tail(5)
                t=df2.x.values[-1]
                model_line.fit(df2.x.values.reshape(-1,1),df2.y.values.reshape(-1,1))
                a  = model_line.intercept_#截距
                a = np.round(a[0],2)
                b = model_line.coef_#迴歸係數
                b = np.round(b[0][0],2)
                print("最佳擬合線: Y = ",a,"+",b,"* X")
                re =  a + b* (t)
                t = int((re+40-a)/b)
                re =  a + b* (t)
                #re =  a + b* (t+re)
                re = int(re)
                print("x:",t,"predict_y:",re)
                prev_list_x.append(t)
                prev_list_y.append(re)
