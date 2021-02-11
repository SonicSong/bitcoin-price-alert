import urllib.request, time
from bs4 import BeautifulSoup
from playsound import playsound
def main():
    print('To stop program press ctrl+c')
    btc_last = '0'
    sleep_max = 0
    while True:
        content = urllib.request.urlopen('https://rate.sx/1BTC')
        read_content = content.read().decode('UTF-8')
        print('USD ' + read_content)
        if read_content <= '46164':
            print('LOW PRICE ALERT!')
            if read_content != btc_last:
                print('PRICE CHANGE!')
                #playsound('SCREAM.mp3')    #mp3 file should be in the same location as bitcoin.py
            btc_last = read_content
        if sleep_max > 150:
            break
        time.sleep(10)
        sleep_max += 1
main()