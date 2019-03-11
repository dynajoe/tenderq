from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"chicken +thigh box kcbs", "no_numbering": True, "color": "brown", "limit":100,"print_urls":True}   #creating list of arguments
response.download(arguments)   #passing the arguments to the function
