import matplotlib.pyplot as plt
import pandas as pd
def direct_link(link):
    """transform sharelink from google drive into a direct link
    
        Keyword arguments:
        link -- A string. The url needed to be pharsed
        
        Output a direct link
    """
    link=link.replace("file/d/","uc?id=")
    link_1=link.split("/view")
    link_1.pop(1)
    link_1.append("&export=download")
    link="".join(link_1)
    return link
def main():

    # Loading data. Dataset is too large for git, therefore hosted on google drive. 
    # read.csv would not work with sharelink so the link need to be phased
    url_F_share='https://drive.google.com/file/d/1-K8-BE6iA2b9FlA7fyg9i5wwidhsVFmR/view?usp=share_link'
    url_G1_share='https://drive.google.com/file/d/1tNn90Z1GpGBemK7_Aj_ILOtGOb6LZF6z/view?usp=share_link'
    url_UK1_share='https://drive.google.com/file/d/1SibXF_igCgND_RUaSJiki9L311LSjZHD/view?usp=share_link'
    url_UK2_share='https://drive.google.com/file/d/1C5ajK4VHf2dac_fNS_ffFWZ1YcrDgP5M/view?usp=share_link'
    
    url_F=direct_link(url_F_share)
    url_G1=direct_link(url_G1_share)
    url_UK1=direct_link(url_UK1_share)
    url_UK2=direct_link(url_UK2_share)
        
    df_F=pd.read_csv(url_F)
    df_G1=pd.read_csv(url_G1)
    df_UK1=pd.read_csv(url_UK1)
    df_UK2=pd.read_csv(url_UK2)
    column_label=df_F.columns
    dataset_label=['df_F','df_G1','df_UK1','df_UK2']
    print("Starting dataframe size:")
    print(df_F.shape)
    print(df_G1.shape)
    print(df_UK1.shape)
    print(df_UK2.shape)

    print(df_F.info(verbose=True))
    nulls_F = df_F[df_F.isnull().any(axis=1)]
    df_F=df_F.drop(nulls_F.index)
    print(nulls_F)
    print(df_F.info(verbose=True))
    
    print(df_G1.info(verbose=True))
    nulls_G1 = df_G1[df_G1.isnull().any(axis=1)]
    print(nulls_G1)
    df_G1=df_G1.drop(nulls_G1.index)
    print(df_G1.info(verbose=True))
    
    print(df_UK1.info(verbose=True))
    nulls_UK1 = df_UK1[df_UK1.isnull().any(axis=1)]
    df_UK1=df_UK1.drop(nulls_UK1.index)
    print(nulls_UK1)
    print(df_UK1.info(verbose=True))
    
    print(df_UK2.info(verbose=True))
    nulls_UK2 = df_UK2[df_UK2.isnull().any(axis=1)]
    df_UK2=df_UK2.drop(nulls_UK2.index)
    print(nulls_UK2)
    print(df_UK2.info(verbose=True))
    
    print("Longitude in dataset:")
    print(df_F["Longitude"].unique())
    print("Latitude in dataset")
    print(df_F["Latitude"].unique())
    
    df_F["Serial_date_number_base_date_1_January_0000"]=round(df_F["Serial_date_number_base_date_1_January_0000"])
    df_F=df_F.drop_duplicates(subset="Serial_date_number_base_date_1_January_0000",keep='first')
    df_F["Serial_date_number_base_date_1_January_0000"]=pd.to_numeric(df_F["Serial_date_number_base_date_1_January_0000"],downcast='integer')
    df_G1["Serial_date_number_base_date_1_January_0000"]=round(df_G1["Serial_date_number_base_date_1_January_0000"])
    df_G1=df_G1.drop_duplicates(subset="Serial_date_number_base_date_1_January_0000",keep='first')
    df_G1["Serial_date_number_base_date_1_January_0000"]=pd.to_numeric(df_G1["Serial_date_number_base_date_1_January_0000"],downcast='integer')
    df_UK1["Serial_date_number_base_date_1_January_0000"]=round(df_UK1["Serial_date_number_base_date_1_January_0000"])
    df_UK1=df_UK1.drop_duplicates(subset="Serial_date_number_base_date_1_January_0000",keep='first')
    df_UK1["Serial_date_number_base_date_1_January_0000"]=pd.to_numeric(df_UK1["Serial_date_number_base_date_1_January_0000"],downcast='integer')
    df_UK2["Serial_date_number_base_date_1_January_0000"]=round(df_UK2["Serial_date_number_base_date_1_January_0000"])
    df_UK2=df_UK2.drop_duplicates(subset="Serial_date_number_base_date_1_January_0000",keep='first')
    df_UK2["Serial_date_number_base_date_1_January_0000"]=pd.to_numeric(df_UK2["Serial_date_number_base_date_1_January_0000"],downcast='integer')
    print("Dataframe size after removing null values and duplicate date:")
    print(df_F.shape)
    print(df_G1.shape)
    print(df_UK1.shape)
    print(df_UK2.shape)
    print(df_F.describe())
    #for loop to create histogram for each column in each dataset
    for x in dataset_label:
        print(x)
        for n in column_label:
            print(n)
            plt.hist(df_F[n])
            plt.show()
    pd.concat([df_F,df_G1,df_UK1,df_UK2]).to_csv('coursework1\data_set_prepared.csv',header=True,index=False)
main()
