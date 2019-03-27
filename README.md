# BingImageSearchScript

Python Image downloading script using Microsoft cognitive services

Create Azure account get you secret key and paste it in the script

`subscription_key = "\ENTER YOU4 CECRET KEY HERE\"`

### Help

```sh
$ python sciptName.py -h

usage: Seach keyword from bing, create folder downlaod images and save it
       [-h] [--s S] [--c C]

optional arguments:

  -h, --help  show this help message and exit
  --s S       Search keyword
  --c C       Image Count
  
```

###  Example Usage download 20 images of apple 

```sh
$ python ImageDownloader.py --s Apple --c 20
```

