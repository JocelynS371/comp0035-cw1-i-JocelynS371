# Data preparation and understanding
## Importing Data
My intial plan was to upload the dataset onto github, then import the csv into my code. However, the file size was too large and the file must be stored on cloud. Therefore, the data is stored on my personal google drive and the url is used to access the data.  

Here the first challenage arised. The link obtained from the drive is a share link. It could not be used in the code, therefore, I looked up how to change a share link into a direct link. The process is written into a function as below:  
```
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
