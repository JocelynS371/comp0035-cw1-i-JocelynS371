# Data preparation and understanding

## Importing Data

My intial plan was to upload the dataset onto github, then import the csv into my code. However, the file size was too large and the file must be stored on cloud. Therefore, the data is stored on my personal google drive and the url is used to access the data.  

Here the first challenage arised. The link obtained from the drive is a share link. It could not be used in the code, therefore, I looked up how to change a share link into a direct link. The process is written into a function as below:  
```python
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
```
This function should work for any google derive sharing link.  

## Inspecting Data

I inspected the size of the data frame. The data size was,
(365011, 8)
(96173, 8)
(719788, 8)
(623956, 8)
respectively. The dataset is too large right now. The first thing we need to do is look for and clean any missing data. Due to the data size, any miss data is omitted rather than replaced.

Note that from here on I will be using only 1 data frame as an example in this mark down file, because the running time is increasing into minutes.

The info method showed no null value in dataframe F, however, A isnull check is done as well to be sure. And null data is dropped. Although there was no null data in F, there was nulls in other dataframe.

## Dropping unnnessary data

Considering that ocean current change on seasonal or yearly timeframe rather than an hourly basis, I decided to keep only 1 data entry per day. Because the date is entered as serial date based 1,Jan,0000. I rounded the number to interger and droped duplicate   
```python
    df_F["Serial_date_number_base_date_1_January_0000"]=round(df_F["Serial_date_number_base_date_1_January_0000"])
    df_F=df_F.drop_duplicates(subset="Serial_date_number_base_date_1_January_0000",keep='first')
    print(df_F)
```   
The dataframe have reduced significantly in size. THe code indicate that   
Starting dataframe size:
(365011, 8)
(96173, 8)
(719788, 8)
(623956, 8)
Dataframe size after removing duplicate date:
(2542, 8)
(661, 8)
(5131, 8)
(4342, 8)
The cleaned data should now be small enough to upload into repository.

## Consideration on serial date

The date is currently stored as a serial date. This is difficult to understand for human, however, it might be convinent for data processing or even machine learning. So after consideraton the date is kept as a serial date.

## Significant figure

A close inspectation of the data would show that the data, especially the temperture, is shown to a very high number of significant figure. This is not uncommon for electrically measured data. However the accuracy at this level is not reliable and it would be more convinent to use less significant figure. Therefore, all the data are rounded to 3 significant figure.