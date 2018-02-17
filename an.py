from __future__ import print_function
import pandas as pd,textacy,os
path=os.getcwd()+'\\output'
try:
    os.stat(path)
except:
 os.mkdir(path)  
def looper(a,b,loca): 
 os.chdir(loca)   
 df=pd.read_csv(a,sep='^')
 m=df.columns.tolist()
 df1=pd.read_csv(b,sep='^')
 n=df1.columns.tolist()


 df2=pd.DataFrame(columns=['Column1','Column2'])
 c=0
 for i in m:
    for j in n:
      if textacy.similarity.jaro_winkler(i,j)>=1:
          c=c+1
          df2.loc[c,'Column1']=i
          df2.loc[c,'Column2']=j
 df2.columns=['Columns for table 1','Columns for table 2'] 
 df3=pd.DataFrame(columns=['S.No','List of columns','Data Type'])  
 df3['Data Type']= [ str(x).replace('64','') for x in list(df.dtypes)]  
 df3['List of columns']=m
 df3['S.No']=list(range(1,len(df3.index)+1))


 df4=pd.DataFrame(columns=['S.No','List of columns','Data Type'])   
 df4['Data Type']=[ str(x).replace('64','') for x in list(df1.dtypes)] 
 df4['List of columns']=n
 df4['S.No']=list(range(1,len(df4.index)+1))

 

 from pandas.core.common import array_equivalent



 def duplicate_columns(frame):
    groups = frame.columns.to_series().groupby(frame.dtypes).groups
    dups = []

    for t, v in groups.items():

        cs = frame[v].columns
        vs = frame[v]
        lcs = len(cs)
       

        for i in range(lcs):
            ia = vs.iloc[:,i].values
            for j in range(i+1, lcs):
                ja = vs.iloc[:,j].values
                if array_equivalent(ia, ja):
                    dups.append(cs[i])
                    break

    return dups


 df6=pd.DataFrame(columns=['Table','Duplicate Columns'])
 i1=duplicate_columns(df)
 i2=duplicate_columns(df1)
 df6.loc[0,'Duplicate Columns']=','.join([x for x in i1])
 df6.loc[1,'Duplicate Columns']=','.join([x for x in i2])
 df6['Table']=[a.replace('.csv',''),b.replace('.csv','')]

 df7=pd.DataFrame(columns=[ 'Number of Rows','Number of Columns'])
 m2=(list(df.shape))

 m2=[m2]
 m3=(list(df1.shape))

 m3=[m3]

 df7=df7.append(pd.DataFrame(m2, columns=[ 'Number of Rows','Number of Columns']),ignore_index=True)
 df7=df7.append(pd.DataFrame(m3, columns=[ 'Number of Rows','Number of Columns']),ignore_index=True)

 df7.insert(loc=0,column='Table',value='')
 df7['Table']=[a.replace('.csv',''),b.replace('.csv','')]


 df8=pd.DataFrame(columns=['Number of Columns','Name of Columns'])
 df8.loc[0,'Name of Columns']=','.join([x for x in( df.columns[df.isna().any()].tolist())])
 df8.loc[1,'Name of Columns']=','.join([x for x in  (df1.columns[df1.isna().any()].tolist())])
 df8.insert(loc=0,column='Table',value='')
 df8['Table']=[a.replace('.csv',''),b.replace('.csv','')]
 df8.loc[0,'Number of Columns']=len(df8.loc[0,'Name of Columns'].split(','))
 df8.loc[1,'Number of Columns']=len(df8.loc[1,'Name of Columns'].split(','))

 a=a.replace('.csv','')
 path1=path+'\\{}'.format(a)

 try:
    os.stat(path1)
 except:
  os.mkdir(path1) 
 b=b.replace('.csv','')
 os.chdir(path1)
 
 writer = pd.ExcelWriter('{}.xlsx'.format(b), engine='xlsxwriter') 
 df2.to_excel(writer,sheet_name="Matching Columns between tables",index=False,engine='c')
 df3.to_excel(writer,sheet_name="Columns for table 1",index=False,engine='c')
 df4.to_excel(writer,sheet_name="Columns for table 2",index=False,engine='c')
 df6.to_excel(writer,sheet_name="Duplicate Columns",index=False,engine='c')
 df7.to_excel(writer,sheet_name="Table Structure",index=False,engine='c')
 df8.to_excel(writer,sheet_name="Columns with Missing Data",index=False,engine='c')

          




