#!/usr/bin/env python
# A python to download a song or a list of songs.
# create by Shivam Sharma

# import all the library used
import re, urllib, os, sys

# determine python version
version = sys.version_info[0]

# set user_input and import modules for correct version of python
if version == 2:  # python 2.x
    user_input = raw_input
    import urllib2
    urlopen = urllib2.urlopen  # open a url
    encode = urllib.urlencode  # encode a search line
    retrieve = urllib.urlretrieve  # retrieve url info
    cleanup = urllib.urlcleanup()  # cleanup url cache

else:  # python 3.x
    user_input = input
    import urllib.request
    import urllib.parse
    urlopen = urllib.request.urlopen
    encode = urllib.parse.urlencode
    retrieve = urllib.request.urlretrieve
    cleanup = urllib.request.urlcleanup()




def screen_clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



def video_title(url):
    try:
        webpage = urlopen(url).read()
        title = str(webpage).split('<title>')[1].split('</title>')[0]
    except:
        title = 'Youtube Song'

    return title

def intro():
    print('''Created by Shivam Sharma
    FB:- shivams334
    Email:- shivams334@gmail.com''')

# download directly with a song name or link
def single_download(song=None):
    if not(song):
        song = user_input('Enter the song name or youtube link: ')  # get the song name from user

    if "youtube.com/" not in song:
        # try to get the search result and exit upon error
        try:
            query_string = encode({"search_query" : song})
            html_content = urlopen("http://www.youtube.com/results?" + query_string)

            if version == 3:  # if using python 3.x
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            else:  # if using python 2.x
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read())
        except:
            print('Network Error')
            return None
        
        # generate a download link that can be used to get the audio file using youtube2mp3 API
        downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video=' + 'http://www.youtube.com/watch?v=' + search_results[0]

    else:      # For a link
        downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video='+song
        song=video_title(song)

    try:
        print('Downloading %s' % song)
        # code a progress bar for visuals? this way is more portable than wget
        retrieve(downloadLinkOnly, filename='%s.mp3' % song)
        cleanup  # clear the cache created by urlretrieve
    except:
        print('Error downloading %s' % song)
        return None

# program exit
def exit(code):
    print('\nExiting....')
    print('\nHave a good day.')
    sys.exit(code)



def main():
    try:
        screen_clear()
        intro()

        try:
            single_download()
        except NameError:
            exit(1)
    except KeyboardInterrupt:
        exit(1)
    exit(1)

if __name__ == '__main__':
    main() 
exit(0) 