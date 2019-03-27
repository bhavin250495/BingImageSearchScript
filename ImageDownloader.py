
import requests
import argparse
import os
       
class Image_Download:

    path = ''

    def createDir(self,name):
        self.path = os.getcwd()+'/'+name
        if not os.path.exists(self.path):
            try:  
                os.mkdir(self.path)
                return True
            except OSError:  
                print ("Creation of the directory %s failed" % self.path)
                return False
        else:
            return True   

    def download_and_save_image(self,url,imgName):
        localDirPath = self.path+'/'+imgName
        f = open(localDirPath,'wb')
        f.write(requests.get(url).content)
        f.close()

    def fire_api(self,search,count):

        subscription_key = "/ENTER YOUR BING API KEY HERE/"
        assert subscription_key

        search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

        headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
        params  = {"q": search,"count":count}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        return search_results['value']

    def __init__(self,search,count = 111):

        value =  self.fire_api(search,count)

        if self.createDir(search):

            for i in range(len(value)):

                thumbnailUrl = value[i]['thumbnailUrl']
                #contentUrl = value[i]['contentUrl']
                imgName= 'img'+str(i)+'.jpg'

                self.download_and_save_image(thumbnailUrl,imgName)

if __name__ == "__main__":

    parser = argparse.ArgumentParser('Seach keyword from bing, create folder downlaod images and save it')
    parser.add_argument('--s',default = 'Bing' ,help='Search keyword',type = str)
    parser.add_argument('--c',default = 10 ,help= 'Image Count',type = int)
    args = parser.parse_args()
    Image_Download(args.s,args.c)