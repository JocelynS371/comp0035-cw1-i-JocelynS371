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

## Seperating data

Before we handle the data further, we need to consider seperating dataset F into F1 and F2. This is because the data source stated that data from 2 mooring site(F1 and F2) is merged into a single dataset F.
After inspecting the location data in dataset F, I concluded that the location is too close together to seperate. The equipment deployment diagram in the data source supported my conclusion.  
 ![Equipment_deployment](\Dataset\Angmagssalik_Mooring_Deployment.png)
We can see from the diagram that the depth at the 2 location are the same and they are only 9km apart from each other according to ressearch. 

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

The date is currently stored as a serial date. This is difficult to understand for human, however, it might be convinent for data processing or even machine learning later in the project. So after consideraton the date is kept as a serial date.

## Managing data type

Now if we look back on the data info. We see that a lot of the data is stored as float. Floating number is an aproximation of real number, they save on storage but accuracy will be lost if we are to use it for calculation.
Our data, in particular temperture and salinity is measured to a very high significant number. Storing them as float might be appropiate as it may take too much memory if we convert it into interger, and slight error in calculations should be tolerable.
However, it might be appropiate to store date, now rounded down, into an interger type. This reduce the possible error and is convinent.
The function used is from to_numeric. Using the parameter downcast, we converted the floating date into a interger date.

## Exploring data

I attempted to spot outlier using the describe function, however, I found the output to be too vague. Therefore, instead of the function, I wrote a for loop to create a histogram for each column in each dataset. There is no obvious outlier and all the continous data followed a rough normal disturbution shape.   
A noticeable point is that the data is missing in some date:  
![Date_Hist]