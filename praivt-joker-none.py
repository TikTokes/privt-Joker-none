import os,socket,json,random
import time
#import logging
import datetime
import telegram
import requests
import urllib.request
from telegram import *
from telegram.ext import *
from telegram.ext import Updater
from pygoogling.googling import GoogleSearch
r = requests.session()
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    level=logging.INFO)
#logger = logging.getLogger(__name__)
print("logging TRUE ...")
IDadmin = "1523692544"
TOKadmin = "1504064676:AAHrqqB0wp529XYruAFFqyZ8ovTteE0defA"
blokID = "1626966367"
blokID2 = "958306236"
new = datetime.datetime.now()
tim = new.strftime('%I:%M %p  [%x]')
TIK,twCHK,b7s,ck,bck,insCK,bck2,hck,pi,Dds,rde,sckn,dn,sub,lnke,gogl,tKin,gteip,trgim,AS3,HIur= range(21)
MAIN, nonr = range(2)
bace1 = [
  [InlineKeyboardButton("GO BACK 🔙", callback_data=str(b7s))]]
bar1 = InlineKeyboardMarkup(bace1)
bace2 = [
    [InlineKeyboardButton("GO BACK 🔙", callback_data=str(hck))]]
bar2 = InlineKeyboardMarkup(bace2)
bace3 = [
    [InlineKeyboardButton("GO BACK 🔙", callback_data=str(AS3))]]
bar3 = InlineKeyboardMarkup(bace3)
def hotmail(update,context):
    global eml
    ms = f"email Linked on hotmail :\n\t{eml}\n𝚂𝙴𝙰𝚁𝙲𝙷 𝙴𝙽𝙳𝙴𝙳 ☑️"
    if "gmail" in eml:
        update.message.bot.send_message(chat_id=update.message.chat_id, text=f"✖️ Not {ms}", reply_markup=bar1)
        return MAIN
    else:
        pass
    url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + eml + "&_=1604288577990"
    data = ''
    headers = {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Connection": "close",
            "Host": "odc.officeapps.live.com",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
            "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
            "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
            "uaid": "d06e1498e7ed4def9078bd46883f187b",
            "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
    html = r.get(url, data=data, headers=headers).text
    if 'Neither' in html:
          update.message.bot.send_message(chat_id=update.message.chat_id,text=f"✖️ Not {ms}", reply_markup=bar1)
          return MAIN
    else:
          update.message.bot.send_message(chat_id=update.message.chat_id,text=f"☑️ {ms}", reply_markup=bar1)
          return MAIN
def EMLtiktok(update,context):
    global eml
    ms = 'Linked to tiktok'
    url = 'https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/?residence=AE&device_id=6923575826752275974&os_version=14.3&app_id=1233&iid=6951746276598204161&app_name=musical_ly&pass-route=1&vendor_id=EF3C1478-2AFC-4B8E-8030-C608120AECF9&locale=ar&pass-region=1&ac=WIFI&sys_region=US&ssmix=a&version_code=17.2.0&vid=EF3C1478-2AFC-4B8E-8030-C608120AECF9&channel=App%20Store&op_region=AE&os_api=18&idfa=00000000-0000-0000-0000-000000000000&install_id=6951746276598204161&idfv=EF3C1478-2AFC-4B8E-8030-C608120AECF9&device_platform=iphone&device_type=iPhone9%2C4&openudid=3ce553bec09070081e5a698d3a14a988f3642ac4&account_region=&tz_name=Asia%2FDubai&tz_offset=14400&app_language=ar&carrier_region=AE&current_region=AE&aid=1233&mcc_mnc=42402&screen_width=1242&uoo=1&content_language=&language=ar&cdid=FBF67CFE-39E1-4556-A3EB-624A20A434E1&build_number=172025&app_version=17.2.0&resolution=1242%2A2208'
    headers = {
        'Host': 'api16-normal-c-alisg.tiktokv.com',
        'Connection': 'close',
        'Content-Length': '76',
        'Cookie': f'sessionid=b0b2ed352b9394eefc29754dfe80926c',
        'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-tt-passport-csrf-token': 'b0b2ed352b9394eefc29754dfe80926c',
        'sdk-version': '2',
        'passport-sdk-version': '5.12.1'}
    data = {
        'account_sdk_source': 'app',
        'email': eml,
        'mix_mode': '1',
        'type': '31'}
    r1 = r.post(url, data=data, headers=headers).text
    if '"message":"success"' in r1:
      update.message.bot.send_message(chat_id=update.message.chat_id,text=f"☑️ {ms}")
      hotmail(update,context)
    elif '"description":"غير مسجل بعد"' in r1:
      update.message.bot.send_message(chat_id=update.message.chat_id,text=f"✖️ Not {ms}")
      hotmail(update,context)
    else:
      update.message.bot.send_message(chat_id=update.message.chat_id,text=f"✖️ Not {ms}")
      hotmail(update,context)
def TWR(update,context):
    global eml
    ms = f"email Linked on twitter :\n\t{eml}"
    urTW = "https://twitter.com/users/email_available?email="+eml
    headTW = {
                'Host': 'twitter.com',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
                'Cookie': 'personalization_id="v1_6TNKT0FSMkPP7CfzL5Rkfg=="; guest_id=v1%3A159789135703778252; _ga=GA1.2.490437195.1597891367'}
    go = r.get(urTW,headers=headTW).text
    if '"taken":true' in go:
      update.message.bot.send_message(chat_id=update.message.chat_id,text=f"☑️ {ms}")
      EMLtiktok(update,context)

    else:
      update.message.bot.send_message(chat_id=update.message.chat_id,text=f"✖️ Not {ms}")
      EMLtiktok(update,context)
def emINS(update,context):
    global eml
    ms = f"email Linked on instagram :\n\t{eml}"
    urIN = 'https://www.instagram.com/accounts/account_recovery_send_ajax/'
    headIN = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '95',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'mid=YHBM1wALAAHufTOe6WaPELkArmSR; ig_did=D3985829-D32C-442A-93B8-884D6D5F21CB; ig_nrcb=1; shbid=8184; shbts=1617972700.0829134; rur=FTW; csrftoken=9YMnthRS1iPDnQjEGY6MHcpC0snKpWyJ',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/password/reset/',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'x-csrftoken': '9YMnthRS1iPDnQjEGY6MHcpC0snKpWyJ',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '3c8826838272',
    'x-requested-with': 'XMLHttpRequest'}
    daIN = {
    'email_or_username': f'{eml}',
    'recaptcha_challenge_field': '',
    'flow': '',
    'app_id': '',
    'source_account_id': ''}
    go = r.post(urIN,headers=headIN,data=daIN).text
    if '"status":"ok"' in go:
      update.message.bot.send_message(chat_id=update.message.chat_id,text=f"☑️ {ms}")
      TWR(update,context)
    else:
      update.message.bot.send_message(chat_id=update.message.chat_id,text=f"✖️ Not {ms}")
      TWR(update,context)
def aple(update,context):
    global eml
    msic = f'Linked on icloud : \n\t{eml}'
    urAP = 'https://iforgot.apple.com/password/verify/appleid'
    headAP = {
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
      'Connection': 'keep-alive',
      'Content-Length': '32',
      'Content-Type': 'application/json',
      'Cookie': 'idclient=web; dslang=SA-AR; site=SAU; X-Apple-I-Web-Token=AAAAKjJ8ZDBjODI2NmQ3YjIyZDlmN2ZkYWY3ZjM5MDYwYThmMzEAAAF4wSw9O2/XviRxkNFZbab0L8x4eDT3GeUoSVFUJALzgCyx6gNTMn1cjnlWAA/f8q9PbWfGM6YdbDBCIUw2q3N3MY+y4O9JmGNrzvpxAqL7/GGlrw==; ifssp=0D2243D3D6F75A646D60C9F045726F9A01DB5B0852CDF5C4731F0907C1018FDDF377E64E0A31AE8A8586FBA0DFCBF0020A3957DD041CECC9EA60150021E4C57809C681FF2EA14B16E0310B42D6413E7C84938A38AE9A560CA96A15867E4DA614B510B513E4DB39D02747FE4E7DC4164E88E564EA603BB1C6; geo=US',
      'Host': 'iforgot.apple.com',
      'Origin': 'https://iforgot.apple.com',
      'Referer': 'https://iforgot.apple.com/',
      'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'sstt': 'eGjzlaNPEoQCz16c5mrfpMuwwob%2FV4K2S6%2BcyK%2BuGsNoqqAIQsu2T8jClaCmWsHUE1EoGLRU6Kkkj6VvGv6jNqSow7SaFHKe%2BVRkMPvqHr4LG32fQCeoQp%2Fxc38mt%2FeTrlLQCanmv9EByQjWZjWkQU3DDk5VM72UQRP%2BEzxmkmOgGzmsLlYklE%2F4tlbSiAqOnNklRiTAiMaWyyCKX69nzCC3NTBCO3ZtSXhwqsI%2BuudVA%2FZ6fd8TB4p1m%2FKtfl8zzh8dmzxmDNaTbh0PaN1ChPwxQqXKZ7%2FBLkFzLJUrgpW6jfF4dv1Dp6o65mwKtGWWf18C3FGUFqwn5isyDMIUFbtReq1vBxqNN%2BJ5b0xQBwvw%2Fv2ian5ZYu3oiKznZcQ2maWl5h7be47I9jCp',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
      'X-Apple-I-FD-Client-Info': '"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36","L":"ar","Z":"GMT+00:00","V":"1.1","F":".8a44j1e3NlY5BNlY5BSmHACVZXnN9.jJcOOFa1c4q8PlHoJR1gJh469LarUqUdHz16um3.I25CFQgB4AL9LXYVpX_cctJ9Xvj9zKqUkaygW.3klY5BNle_5BNlan0Os5Apw.3JW"',
      'X-Requested-With': 'XMLHttpRequest'}
    daAP = {'id': f'{eml}'}
    go = r.post(urAP,headers=headAP,json=daAP)
    if go.status_code == 200:
      update.message.bot.send_message(chat_id=update.message.chat_id,text=f"☑️ {msic}")
      emINS(update,context)
    else:
      update.message.bot.send_message(chat_id=update.message.chat_id,text=f"✖️ Not {msic}")
      emINS(update,context)
def SNPEML(update,context):
    global eml
    eml = ' '.join(context.args)
    if eml == "":
        update.message.bot.send_message(chat_id=update.message.chat_id, text="Please enter a website link !", reply_markup=bar1)
        return MAIN
    else:
        ms = f"email Linked on snapchat :\n\t{eml}"
        urSN = 'https://accounts.snapchat.com/accounts/merlin/login'
        headSP = {
          'accept': 'application/json, text/plain, */*',
          'accept-encoding': 'gzip, deflate, br',
          'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
          'content-length': '57',
          'content-type': 'application/json',
          'cookie': 'xsrf_token=lNCAQwlKxAFUR6TW1Pfslw; web_client_id=ef2cf884-fe98-4193-bafe-be168920059c',
          'origin': 'https://accounts.snapchat.com',
          'referer': 'https://accounts.snapchat.com/accounts/merlin/login',
          'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
          'sec-ch-ua-mobile': '?0',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
          'x-xsrf-token': 'lNCAQwlKxAFUR6TW1Pfslw'}
        daSP = {
          'app': 'BITMOJI_APP',
          'email': f'{eml}'}
        go = r.post(urSN,headers=headSP,json=daSP).text
        if '"hasSnapchat": true' in go:
          update.message.bot.send_message(chat_id=update.message.chat_id,text=f"☑️ {ms}")
          aple(update,context)
        else:
          update.message.bot.send_message(chat_id=update.message.chat_id,text=f"✖️ Not {ms}")
          aple(update,context)
def tellm(update,context):
    global user ,msgSN,msgIN,msdisqus,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND,msvime,msgoodr,msspotify,mswordp,mspast,msgitlab,msfour,msflickr,msycomb,msslack,msbitb,mspinter
    query = update.callback_query
    urTM = f'https://tellonym.me/{user}'
    headTM = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': '',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
    go = r.get(urTM, headers=headTM)
    if go.status_code == 200:
        msgtem = f"""☑️ Linked on tellonym : {user}

SEARCH ENDED 🔘
            """
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}\n{msflickr}\n{msycomb}\n{msslack}\n{msbitb}\n{mspinter}\n{msdisqus}\n{msgtem}",reply_markup=bar1)
        return MAIN
    else:
        msgtem = f"""✖️ Not Linked on tellonym : {user}

SEARCH ENDED 🔘
            """
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}\n{msflickr}\n{msycomb}\n{msslack}\n{msbitb}\n{mspinter}\n{msdisqus}\n{msgtem}",reply_markup=bar1)
        return MAIN
def disqus(update,context):
    global user ,msgSN,msgIN,msdisqus,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND,msvime,msgoodr,msspotify,mswordp,mspast,msgitlab,msfour,msflickr,msycomb,msslack,msbitb,mspinter
    query = update.callback_query
    time.sleep(0.4)
    msdisqus = f"Linked to disqus {user}"
    link = {'https://disqus.com'}
    for user2 in link :
      user3 = user2+"/"+user
      try:
        openurl = urllib.request.urlopen(user3)
        msdisqus = f"☑️ Linked to disqus {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}\n{msflickr}\n{msycomb}\n{msslack}\n{msbitb}\n{mspinter}\n{msdisqus}",reply_markup=bar1)

        tellm(update,context)
      except urllib.error.URLError as msg :
        msdisqus = f"✖️ Not Linked to disqus {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}\n{msflickr}\n{msycomb}\n{msslack}\n{msbitb}\n{mspinter}\n{msdisqus}",reply_markup=bar1)

        tellm(update,context)
def pinter(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND,msvime,msgoodr,msspotify,mswordp,mspast,msgitlab,msfour,msflickr,msycomb,msslack,msbitb,mspinter
    query = update.callback_query
    time.sleep(0.4)
    link = {'https://www.pinterest.com'}
    for user2 in link :
      user3 = user2+"/"+user
      try:
        openurl = urllib.request.urlopen(user3)
        mspinter = f"☑️ Linked to pinterest {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}\n{msflickr}\n{msycomb}\n{msslack}\n{msbitb}\n{mspinter}",reply_markup=bar1)
        disqus(update,context)
      except urllib.error.URLError as msg :
        mspinter = f"✖️ Not Linked to pinterest {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}\n{msflickr}\n{msycomb}\n{msslack}\n{msbitb}\n{mspinter}",reply_markup=bar1)
        disqus(update,context)
def bitb(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND,msvime,msgoodr,msspotify,mswordp,mspast,msgitlab,msfour,msflickr,msycomb,msslack,msbitb
    query = update.callback_query
    time.sleep(0.4)
    msbitb = f"Linked to bitbucket {user}"
    link = {'https://bitbucket.org'}
    for user2 in link :
      user3 = user2+"/"+user
      try:
        openurl = urllib.request.urlopen(user3)
        msbitb = f"☑️ Linked to bitbucket {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}\n{msflickr}\n{msycomb}\n{msslack}\n{msbitb}",reply_markup=bar1)
        pinter(update,context)
      except urllib.error.URLError as msg :
        msbitb = f"✖️ Not Linked to bitbucket {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}\n{msflickr}\n{msycomb}\n{msslack}\n{msbitb}",reply_markup=bar1)
        pinter(update,context)
def slack(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND,msvime,msgoodr,msspotify,mswordp,mspast,msgitlab,msfour,msflickr,msycomb,msslack
    query = update.callback_query
    time.sleep(0.4)
    link = {'https://slack.com'}
    for user2 in link :
      user3 = user2+"/"+user
      try:
        openurl = urllib.request.urlopen(user3)
        msslack = f"☑️ Linked to slack {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}\n{msflickr}\n{msycomb}\n{msslack}",reply_markup=bar1)
        bitb(update,context)
      except urllib.error.URLError as msg :
        msslack = f"✖️ Not Linked to slack {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}\n{msflickr}\n{msycomb}\n{msslack}",reply_markup=bar1)
        bitb(update,context)
def ycomb(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND,msvime,msgoodr,msspotify,mswordp,mspast,msgitlab,msfour,msflickr,msycomb
    query = update.callback_query
    time.sleep(0.4)
    link = {'https://news.ycombinator.com/user?id='}
    for user2 in link :
      user3 = user2+"/"+user
      try:
        openurl = urllib.request.urlopen(user3)
        msycomb = f"☑️ Linked to ycombinator {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}\n{msflickr}\n{msycomb}",reply_markup=bar1)
        slack(update,context)
      except urllib.error.URLError as msg :
        msycomb = f"✖️ Not Linked to ycombinator {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}\n{msflickr}\n{msycomb}",reply_markup=bar1)
        slack(update,context)
def flickr(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND,msvime,msgoodr,msspotify,mswordp,mspast,msgitlab,msfour,msflickr
    query = update.callback_query
    time.sleep(0.4)
    msflickr = "Linked to flickr"
    link = {'https://www.flickr.com/people'}
    for user2 in link :
      user3 = user2+"/"+user
      try:
        openurl = urllib.request.urlopen(user3)
        msflickr = f"☑️ Linked to flickr {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}\n{msflickr}",reply_markup=bar1)
        ycomb(update,context)
      except urllib.error.URLError as msg :
        msflickr = f"✖️ Not Linked to flickr {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}\n{msflickr}",reply_markup=bar1)
        ycomb(update,context)
def four(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND,msvime,msgoodr,msspotify,mswordp,mspast,msgitlab,msfour
    query = update.callback_query
    time.sleep(0.4)
    link = {'https://foursquare.com'}
    for user2 in link :
      user3 = user2+"/"+user
      try:
        openurl = urllib.request.urlopen(user3)
        msfour = f"☑️ Linked to foursquare {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}",reply_markup=bar1)
        flickr(update,context)
      except urllib.error.URLError as msg :
        msfour = f"✖️ Not Linked to foursquare {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}\n{msfour}",reply_markup=bar1)
        flickr(update,context)
def gitlab(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND,msvime,msgoodr,msspotify,mswordp,mspast,msgitlab
    query = update.callback_query
    time.sleep(0.4)
    link = {'https://gitlab.com'}
    for user2 in link :
      user3 = user2+"/"+user
      try:
        openurl = urllib.request.urlopen(user3)
        msgitlab = f"☑️ Linked to gitlab {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}",reply_markup=bar1)
        four(update,context)
      except urllib.error.URLError as msg :
        msgitlab = f"✖️ Not Linked to gitlab {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}\n{msgitlab}",reply_markup=bar1)
        four(update,context)
def past(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND,msvime,msgoodr,msspotify,mswordp,mspast
    query = update.callback_query
    time.sleep(0.4)
    link = {'https://pastebin.com/u'}
    for user2 in link :
      user3 = user2+"/"+user
      try:
        openurl = urllib.request.urlopen(user3)
        mspast = f"☑️ Linked to pastebin {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}",reply_markup=bar1)
        gitlab(update,context)
      except urllib.error.URLError as msg :
        mspast = f"✖️ Not Linked to pastebin {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}\n{mspast}",reply_markup=bar1)
        gitlab(update,context)
def wordp(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND,msvime,msgoodr,msspotify,mswordp
    query = update.callback_query
    time.sleep(0.4)
    link = {'https://wordpress.com'}
    for user2 in link :
      user3 = user2+"/"+user
      try:
        openurl = urllib.request.urlopen(user3)
        mswordp = f"☑️ Linked to wordpress {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}",reply_markup=bar1)
        past(update,context)
      except urllib.error.URLError as msg :
          mswordp = f"✖️ Not Linked to wordpress {user}"
          query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}\n{mswordp}",reply_markup=bar1)
          past(update,context)
def spotify(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND,msvime,msgoodr,msspotify
    query = update.callback_query
    time.sleep(0.4)
    link = {'https://open.spotify.com/user'}
    for user2 in link :
      user3 = user2+"/"+user
      try:
        openurl = urllib.request.urlopen(user3)
        msspotify = f"☑️ Linked to spotify {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}",reply_markup=bar1)
        wordp(update, context)
      except urllib.error.URLError as msg :
          msspotify = f"✖️ Not Linked to spotify {user}"
          query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}\n{msspotify}",reply_markup=bar1)
          wordp(update,context)
def goodr(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND,msvime,msgoodr
    query = update.callback_query
    time.sleep(0.4)
    link = {'https://www.goodreads.com'}
    for user2 in link :
      user3 = user2+"/"+user
      try:
        openurl = urllib.request.urlopen(user3)
        msgoodr = "☑️ Linked to goodreads"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}",reply_markup=bar1)
        spotify(update,context)
      except urllib.error.URLError as msg :
          msgoodr = "✖️ Not Linked to goodreads"
          query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}\n{msgoodr}",reply_markup=bar1)
          spotify(update,context)
def vimeo(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND,msvime
    query = update.callback_query
    time.sleep(0.4)
    link = {'https://vimeo.com'}
    for user2 in link :
      user3 = user2+"/"+user
      try:
        openurl = urllib.request.urlopen(user3)
        msvime = f"☑️ Linked to vimeo {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}",reply_markup=bar1)
        goodr(update,context)
      except urllib.error.URLError as msg :
          msvime = f"✖️ Not Linked to vimeo {user}"
          query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}\n{msvime}",reply_markup=bar1)
          goodr(update, context)
def sond(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT,msSND
    query = update.callback_query
    time.sleep(0.4)
    link = {'https://soundcloud.com'}
    for user2 in link :
      user3 = user2+"/"+user
      try:
        openurl = urllib.request.urlopen(user3)
        msSND = f"☑️ Linked to soundcloud {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}" ,reply_markup=bar1)
        vimeo(update,context)
      except urllib.error.URLError as msg :
          msSND = f"✖ Not Linked to soundcloud {user}"
          query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}\n{msSND}" ,reply_markup=bar1)
          vimeo(update, context)
def yout(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms,msYUT
    query = update.callback_query
    time.sleep(0.4)
    link = {'https://www.youtube.com/user'}
    for user2 in link :
      user3 = user2+"/"+user
      try :
        openurl = urllib.request.urlopen(user3)
        msYUT = f"☑️ Linked to youtobe {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}",reply_markup=bar1)
        sond(update,context)
      except urllib.error.URLError as msg :
        msYUT = f"✖ Not Linked to youtobe {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}\n{msYUT}",reply_markup=bar1)
        sond(update,context)
def face(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth,ms
    query = update.callback_query
    time.sleep(0.4)
    link = {'https://www.facebook.com'}
    for user2 in link :
      user3 = user2+"/"+user
      try :
        openurl = urllib.request.urlopen(user3)
        ms = f"☑️ Linked to Facebook {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}",reply_markup=bar1)
        yout(update, context)
      except urllib.error.URLError as msg :
          ms = f"✖ Not Linked to Facebook {user}"
          query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}\n{ms}", reply_markup=bar1)
          yout(update,context)
def gitHB(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh,megth
    query = update.callback_query
    url = f'https://github.com/{user}'

    go=r.get(url)

    if go.status_code == 200:
        megth = f'☑️ Linked to github : {user}'
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}", reply_markup=bar1)
        face(update, context)
    else:
        megth = f'✖ Not Linked on github : {user}'
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}\n{megth}", reply_markup=bar1)
        face(update,context)
def TWSH(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK,msTh
    time.sleep(0.4)
    query = update.callback_query
    urTH = f'https://m.twitch.tv/{user}'
    hedTH = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
      'Cache-Control': 'max-age=0',
      'Connection': 'keep-alive',
      'Cookie': '',
      'Host': 'm.twitch.tv',
      'If-None-Match': '"471db-/+jglcEK7ZZNdG+AIGCb6DuFU8k"',
      'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'Sec-Fetch-Dest': 'document',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-User': '?1',
      'Service-Worker-Navigation-Preload': 'true',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    go = r.get(urTH,headers=hedTH)
    if go.status_code == 200:
        msTh = f'☑️ Linked on twitch : {user}'
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}", reply_markup=bar1)
        gitHB(update,context)
    else:
        msTh = f'✖️ Not Linked on twitch : {user}'
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}\n{msTh}", reply_markup=bar1)
        gitHB(update,context)
def tiktok(update,context):
    global user ,msgSN,msgIN,msgt,msgTW,msgTIK
    time.sleep(0.4)
    query = update.callback_query
    urCH = f'https://www.tiktok.com/@{user}?'
    hedCH = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                    'cache-control': 'max - age = 0',
                    'sec-ch-ua': '"Google Chrome";v = "89", "Chromium";v = "89", ";Not A Brand";v = "99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    go1 = r.get(urCH,headers=hedCH)
    if go1.status_code == 404:
        msgTIK = f"✖️ Not Linked on tiktok : {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}", reply_markup=bar1)
        tellm(update,context)
    elif go1.status_code == 200:
        msgTIK = f"☑️ Linked on tiktok : {user}"
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}\n{msgTIK}", reply_markup=bar1)
        TWSH(update,context)
    else:
        print('The connection has been blocked !!')
        TWSH(update,context)
def SNP(update,context):
    global user ,msgSN,msgIN,msgt,msgTW
    query = update.callback_query
    time.sleep(0.4)
    urSN = f'https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={user}&xsrf_token=_W2GHDQLlCXbXPlWAMuOeQ'
    headSN = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept": "/",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://accounts.snapchat.com/",
        "Cookie": "xsrf_token=_W2GHDQLlCXbXPlWAMuOeQ; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
    go = r.post(urSN,headers=headSN).text
    if '"status_code":"TAKEN"' in go:
        msgSN = f'☑️Linked on snapchat : {user}'
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}", reply_markup=bar1)
        tiktok(update,context)
    else:
        msgSN = f'✖ Not Linked on snapchat : {user}'
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}\n{msgSN}", reply_markup=bar1)
        tiktok(update,context)
def insta(update,context):
    global user,msgIN,msgt,msgTW
    query = update.callback_query
    time.sleep(0.4)
    url = f'https://instagram.com/{user}'
    headeIN = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'mid=YHBM1wALAAHufTOe6WaPELkArmSR; ig_did=D3985829-D32C-442A-93B8-884D6D5F21CB; ig_nrcb=1; csrftoken=lSXyFDnvL6AwiMTpP7mRJCSQdaxsEwta; ds_user_id=45872034997; sessionid=45872034997%3Aiph3YqS2xJNn9M%3A20; shbid=8184; shbts=1617972700.0829134; rur=FTW',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    go = r.get(url,headers=headeIN)
    if go.status_code == 200:
        msgIN = f'☑️Linked on instagram : {user}'
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}", reply_markup=bar1)
        SNP(update,context)
        return MAIN
    elif go.status_code == 404:
        msgIN = f'✖️ Not Linked on instagram : {user}'
        query.edit_message_text(text=f"{msgt}\n{msgTW}\n{msgIN}", reply_markup=bar1)
        SNP(update,context)
def twitr(update,context):
    global user,msgt,msgTW
    query = update.callback_query
    time.sleep(0.4)
    urWT = "https://tweeterid.com/ajax.php"
    headWT = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '11',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '',
        'origin': 'https://tweeterid.com',
        'referer': 'https://tweeterid.com/',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'}
    daWT = {'input': f'{user}'}
    go = r.post(urWT,headers=headWT,data=daWT)
    if 'error' in go.text:
        msgTW = f'Not Linked on twitter: {user}'
        query.edit_message_text(text=f"{msgt}\n{msgTW}", reply_markup=bar1)
        insta(update,context)
    else:
        msgTW = f'☑️ Linked on twitter: {user}'
        query.edit_message_text(text=f"{msgt}\n{msgTW}", reply_markup=bar1)
        insta(update,context)
def teleegg(update,context: CallbackContext):
    global user,msgt
    query = update.callback_query
    url = f"https://t.me/{user}"
    req = r.get(url)
    if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
        msgt = f'✖️Not Linked on telegram : {user}'
        query.edit_message_text(text=f"{msgt}", reply_markup=bar1)
        twitr(update,context)
    else:
        msgt = f'☑️ Linked on telegram : {user}'
        query.edit_message_text(text=f"{msgt}", reply_markup=bar1)
        twitr(update,context)
def teleg(update,context  ):
    global user
    user = ' '.join(context.args)
    Keyboard = [
        [InlineKeyboardButton("Yes", callback_data=str(rde))],
        [InlineKeyboardButton("GO BACK", callback_data=str(b7s))]]
    okr = InlineKeyboardMarkup(Keyboard)
    if user == "":
        update.message.bot.send_message(chat_id=update.message.chat_id, text="Please enter username !", reply_markup=bar1)
        return MAIN
    else:
        update.message.reply_text(text=f"START ?", reply_markup=okr)
        return  MAIN
def Login(update,context  ):
    tarr = ' '.join(context.args)
    tar =str(tarr)
    if tar == "":
        update.message.bot.send_message(chat_id=update.message.chat_id, text="Please enter username !", reply_markup=bar1)
        return MAIN
    else:
        hd = {
            "Host": "www.instagram.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Cookie": "csrftoken=missing; sessionid=46161793416%3AE7amJ4fIGA21Cz%3A17; shbid=1146; shbts=1619348936.920095; rur=RVA",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
            "Accept-Language": "en-us",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"}
        try:
            import json
            go = requests.get(f"https://www.instagram.com/{tar}/?__a=1", headers=hd)
            ID = json.loads(go.text)["graphql"]["user"]["id"]
            name = json.loads(go.text)["graphql"]["user"]['full_name']
            follow = json.loads(go.text)["graphql"]["user"]['edge_followed_by']['count']
            follog = json.loads(go.text)["graphql"]["user"]['edge_follow']['count']
            urPH = json.loads(go.text)["graphql"]["user"]['profile_pic_url_hd']
            prt = json.loads(go.text)["graphql"]["user"]['is_private']
            msg = f"""
User ID : {ID}
Full name : {name}
Followers : {follow}
Following : {follog}
Private Account : {prt}
Profile Picture : \n{urPH}
          """
            update.message.bot.send_message(chat_id=update.message.chat_id, text=f"{msg}", reply_markup=bar1)
            return MAIN
        except KeyError:
            ms = 'Please check the account entered !'
            update.message.bot.send_message(chat_id=update.message.chat_id, text=f"{ms}", reply_markup=bar1)
            return MAIN
def emils(update,context  ):
    email = ' '.join(context.args)
    if email == "":
        update.message.bot.send_message(chat_id=update.message.chat_id, text="Please enter email !", reply_markup=bar1)
        return MAIN
    else:
        url = 'https://digibody.avast.com/v1/web/email/subscribe'
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '29',
            'Content-Type': 'application/json;charset=UTF-8',
            'Host': 'digibody.avast.com',
            'Origin': 'https://www.avast.com',
            'Referer': 'https://www.avast.com/',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
        data = {'email': f'{email}'}
        ok = r.post(url, headers=headers, json=data)
        if '"already_subscribed":false' in ok.text:
            ms = f"""
    𝐸𝑀𝐴𝐼𝐿 𝐼𝑆 𝑁𝑂𝑇 𝐿𝐸𝐴𝐾𝐸𝐷 ☑️
    {email}
    
    𝐶𝑂𝑀𝑃𝐿𝐸𝑇𝐸𝐷 🔘
            """
            update.message.bot.send_message(chat_id=update.message.chat_id, text=f"{ms}", reply_markup=bar1)
            return MAIN
        elif '"already_subscribed":true' in ok.text:
            ms = f"""
    𝐸𝑀𝐴𝐼𝐿 𝐼𝑆 𝐿𝐸𝐴𝐾𝐸𝐷 📛️
    {email}
    
    𝐶𝑂𝑀𝑃𝐿𝐸𝑇𝐸𝐷 🔘
            """
            update.message.bot.send_message(chat_id=update.message.chat_id, text=f"{ms}", reply_markup=bar1)

            return MAIN
def checEml(update,context  ):
    query = update.callback_query
    ms = """
CHECK IF EMAIL IS LEAKED OR NOT

Enter the email after the /check
Example :
/check joker@gmail.com
    """
    query.edit_message_text(text=f"{ms}", reply_markup=bar1)
    return MAIN
def instU(update,context  ):
    query = update.callback_query
    ms = """
RETRACT INSTAGRAM ACCOUNT 
INFORMATION 

Enter the username person 
after the /user
Example :
/user t.uo
    """
    query.edit_message_text(text=f"{ms}", reply_markup=bar1)
    return MAIN
def Twit(update,context  ):
    query = update.callback_query
    ms = """
SEARCH FOR USERNAME IN THE SITES

Enter the username 
after the /target
Example :
/target vv1ck
        """
    query.edit_message_text(text=f"{ms}", reply_markup=bar1)
    return MAIN
def subdom(update,context  ):
    target = ' '.join(context.args)
    if target == "":
        update.message.bot.send_message(chat_id=update.message.chat_id, text="Please enter a website link !", reply_markup=bar2)
        return MAIN
    else:
        go = r.get('http://api.hackertarget.com/subnetcalc/?q='+target).text
        update.message.bot.send_message(chat_id=update.message.chat_id,text=f'{go}', reply_markup=bar2)
        return MAIN
def scanr(update,context  ):
    target = ' '.join(context.args)
    if target == "":
        update.message.bot.send_message(chat_id=update.message.chat_id, text="Please enter a website link !", reply_markup=bar2)
        return MAIN
    else:
        try:
            ip = socket.gethostbyname(target)
            go = r.get('https://api.hackertarget.com/nmap/?q='+ip).text
            update.message.bot.send_message(chat_id=update.message.chat_id,text=f'{go}', reply_markup=bar2)
            return MAIN
        except:
            ms = "Please enter a valid link or IP"
            update.message.bot.send_message(chat_id=update.message.chat_id, text=f'{ms}', reply_markup=bar2)
            return MAIN
def scans(update,context  ):
    query = update.callback_query
    ms = """
Enter the IP or website url 
after the /scanner
Example :
/scanner www.joker.com
or
/scanner 129.82.6
        """
    query.edit_message_text(text=f"{ms}", reply_markup=bar2)
    return MAIN
def ipp(update,context):
    IP = ' '.join(context.args)
    if IP == "":
        update.message.bot.send_message(chat_id=update.message.chat_id, text="Please enter IP !", reply_markup=bar2)
        return MAIN
    else:
        try:
            Locat = r.get("https://get.geojs.io/v1/ip/geo/"+IP+".json")
            loc  = Locat.json()
            iP   = loc["ip"]
            cot  = loc["country"]
            code  = loc["country_code"]
            zone = loc["timezone"]
            Long = loc["longitude"]
            Lat  = loc["latitude"]
            tar = f"""
        IP ADDRESS : {iP}
          ━━━━━━━━━━━━━
        LOCATION    : {cot}
          ━━━━━━━━━━━━━
        TIMEZONE   : {zone}
          ━━━━━━━━━━━━━
        COUNTRY CODE : {code}
          ━━━━━━━━━━━━━
        LATITUDE ON A MAP : {Lat}
          ━━━━━━━━━━━━━
        LONGITUDE ON A MAP  : {Long}
          """
            update.message.bot.send_message(chat_id=update.message.chat_id,text=f'{tar}', reply_markup=bar2)
            return MAIN
        except:
            ms = "Please enter a valid IP"
            update.message.bot.send_message(chat_id=update.message.chat_id, text=f'{ms}', reply_markup=bar2)
            return MAIN
def ppi(update,context):
    query = update.callback_query
    ms = """
    -------------
Enter the person IP after the /ip
Example :
/ip 129.7.7.10
------------
        """
    query.edit_message_text(text=f"{ms}", reply_markup=bar2)
    return MAIN
def subD(update,context):
    query = update.callback_query
    ms = """
Enter the website url after the /sub
Example :
/sub www.joker.com
        """
    query.edit_message_text(text=f"{ms}", reply_markup=bar2)
    return MAIN
def tools(update,context):
    query = update.callback_query
    ms = """
Enter the email after the /email
Example :
/email joker@gmail.com
        """
    query.edit_message_text(text=f"{ms}", reply_markup=bar1)
    return MAIN
def linkpge(update,context):
    web = ' '.join(context.args)
    if web == "":
        update.message.bot.send_message(chat_id=update.message.chat_id, text="Please enter a website link !",reply_markup=bar2)
        return MAIN
    else:
        try:
            go = r.get('https://api.hackertarget.com/pagelinks/?q=' + web).text
            update.message.bot.send_message(chat_id=update.message.chat_id,text=f'{go}', reply_markup=bar2)
            return MAIN
        except:
            ma = "The bot has been banned due to its heavy use today"
            update.message.bot.send_message(chat_id=update.message.chat_id,text=f'{ma}', reply_markup=bar2)
            return MAIN
def ling(update,context  ):
    query = update.callback_query
    ms = """
Enter the website link after the /link
Example :
/link www.joker.com
        """
    query.edit_message_text(text=f"{ms}", reply_markup=bar2)
    return MAIN
def UL2(update,context):
    global url,url2
    chars2 = 'eobqxiqwertyuiopasdfghjklzxcvbnm'
    amount = 5000
    amount = int(amount)
    length2 = 6
    length2 = int(length2)
    for email in range(amount):
        email = ''
    for item in range(length2):
        email = ''
    for item in range(length2):
        email += random.choice(chars2)
    code = email
    url3 = 'https://v.ht/processreq.php'
    headers={
    'Accept': '*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.5',
    'Connection':'keep-alive',
    'Content-Length':'56',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'_ga=GA1.2.935898743.1617987048; PHPSESSID=c9a502db8cc1b3095432bf06e6e8439f; __utma=80914128.935898743.1617987048.1619153599.1619153599.1; __utmb=80914128.1.10.1619153599; __utmc=80914128; __utmz=80914128.1619153599.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1',
    'Host':'v.ht',
    'Origin':'https://v.ht',
    'Referer':'https://v.ht/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'X-Requested-With':'XMLHttpRequest'}
    data={
        "txt_url": url,"txt_name": f"{code}"}
    go = r.post(url3,headers=headers,data=data)
    if "You can make sure, it's properly working by clicking on it"in go.text:
      msg=f"""
Been completed ☑️
[0] The old url :\n{url}
[1] The new url :\n{url2}
[2] The new url :\nhttps://v.ht/{code}"""
      update.message.bot.send_message(chat_id=update.message.chat_id, text=f"{msg}", reply_markup=bar3)
      return MAIN
    else:
      ms = f"""
Been completed ☑️
[0] The old url :\n{url}
[1] The new url :\n{url2}"""
      update.message.bot.send_message(chat_id=update.message.chat_id, text=f"{ms}", reply_markup=bar3)
      return MAIN
def UL1(update,context):
    global url,url2
    url = ' '.join(context.args)
    if url =="":
      print('You must enter the url')
    else:
      try:
        url2=r.get("https://tinyurl.com/api-create.php?url="+url).text
        if 'Error' in url2:
          ms='Please enter a valid url'
          update.message.bot.send_message(chat_id=update.message.chat_id, text=f"{ms}", reply_markup=bar1)
          return MAIN
        else:
          UL2(update,context)
      except:
        mg = "An unknown error has occurred!"
        update.message.bot.send_message(chat_id=update.message.chat_id, text=f"{mg}", reply_markup=bck)
        return MAIN
def UR3(update,context):
    query = update.callback_query
    ms = """
Enter the link after the /hide
Example : 
/hide https://insta.com/t.uo
            """
    query.edit_message_text(text=f"{ms}", reply_markup=bar3)
    return MAIN
def ddns(update,context):
    target = ' '.join(context.args)
    if target == "":
        update.message.bot.send_message(chat_id=update.message.chat_id, text="Please enter a website link !", reply_markup=bar2)
        return MAIN
    else:
        go = r.get('https://api.hackertarget.com/dnslookup/?q=' + target).text
        update.message.bot.send_message(chat_id=update.message.chat_id,text=f'{go}', reply_markup=bar2)
        return MAIN
def dne(update,context  ):
    query = update.callback_query
    ms = """
Enter the website link after the /dns
Example :
/dns www.joker.com
        """
    query.edit_message_text(text=f"{ms}", reply_markup=bar2)
    return MAIN
def doos(update,context):
    query = update.callback_query
    ms = """
عذرا لايسمح باستخدام هذي الاداة
تم اخفائها لاسباب خاصة
        """
    query.edit_message_text(text=f"{ms}", reply_markup=bar2)
    return MAIN
def Google(update,context):
    email = ' '.join(context.args)
    if email == "":
        update.message.bot.send_message(chat_id=update.message.chat_id, text="Please enter something to search 💢", reply_markup=bar1)
        return MAIN
    else:
        update.message.bot.send_message(chat_id=update.message.chat_id, text="wait a little bit ⏱")
        tst = GoogleSearch
        search = tst("allintext:"+email+"")
        search.start_search(max_page=1)
        search.start_search(max_page=2)
        search.start_search(max_page=3)
        for x in search.search_result:
            done1 = x
            update.message.bot.send_message(chat_id=update.message.chat_id, text=f"Been searched ☑️\n{done1}", reply_markup=bar1)
            return MAIN
def TIKinfo(update,context):
    user = ' '.join(context.args)
    if user=="":
        update.message.bot.send_message(chat_id=update.message.chat_id, text="Please enter username !",reply_markup=bar1)
        return MAIN
    else:
        url = f'https://raven-apis.tech/tiktok?username={user}'
        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}

        go = r.get(url,headers=headers)
        if '"Error"'in go.text:
            print('Please enter a valid username !')
        elif '"Support Server"' in go.text:
            tikIN = json.loads(go.text)
            folow = tikIN['followerCount']
            folog = tikIN['followingCount']
            lik = tikIN['likeCount']
            vid = tikIN['video_count']
            ms =f"""
username: {user}
Followers: {folow}
following: {folog}
Number of videos: {vid}
The number of likes: {lik}
          """
            update.message.bot.send_message(chat_id=update.message.chat_id, text=f"Account Information 🔘\n{ms}", reply_markup=bar1)
            return MAIN
        else:
            update.message.bot.send_message(chat_id=update.message.chat_id,text="Please enter a valid username !",reply_markup=bar1)
            return MAIN
def TIKnfo(update,context):
    query = update.callback_query
    ms = """
Pull tiktok account information

Enter Username After the /tiktok
Example :
/tiktok 6e6k
        """
    query.edit_message_text(text=f"{ms}", reply_markup=bar1)
    return MAIN
def gtIPP(update,context):
    url = ' '.join(context.args)
    try:
      if url =="":
        ms ="Please enter a website link"
        update.message.bot.send_message(chat_id=update.message.chat_id,text=f"{ms}",reply_markup=bar2)
        return MAIN
      else:
        IP = socket.gethostbyname(url)
        update.message.bot.send_message(chat_id=update.message.chat_id,text=f"IP the website :\n{IP}",reply_markup=bar2)
        return MAIN
    except:
        psg = """
Please enter the url of the website correctly
Make sure that the beginning of the written url is www  """
        update.message.bot.send_message(chat_id=update.message.chat_id, text=f"{psg}", reply_markup=bar2)
        return MAIN
def gtip(update,context):
    query = update.callback_query
    ms = """
Enter the url of the site 
after the /get_ip
Example:
/get_ip www.vv1ck.com
"""
    query.edit_message_text(text=f"{ms}", reply_markup=bar2)
    return MAIN
def gogle(update,context):
    query = update.callback_query
    ms = """
To search on Google for anything you want more accurately

Enter anything you want to search for after the /google
Example:
/google mohamed
or
/google imove joker
or
/google image joker
or
/google mohamed@gmail.com
        """
    query.edit_message_text(text=f"{ms}", reply_markup=bar1)
    return MAIN
def Aso3e(update,context):
    query = update.callback_query
    Keyboard = [
        [InlineKeyboardButton("HIDE LINK 🔗", callback_data=str(HIur))],
        [InlineKeyboardButton("قريبا ✖️", callback_data="قلنا قريبا "),
        InlineKeyboardButton("قريبا ✖️", callback_data="قلنا قريبا ")],
        [InlineKeyboardButton("قريبا ✖️", callback_data="قلنا قريبا "),
        InlineKeyboardButton("قريبا ✖️", callback_data="قلنا قريبا ")],
        [InlineKeyboardButton("GO BACK 🔙", callback_data=str(bck))]]
    ms = """  
</>RANDOM TOOLS 🔘
        """
    okr = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{ms}", reply_markup=okr)
    return MAIN
def hack(update,context):
    query = update.callback_query
    Keyboard = [
        [InlineKeyboardButton("SEARCH FOR IP 👁‍🗨", callback_data=str(pi)),
         InlineKeyboardButton("GET IP HTE SITE✔", callback_data=str(gteip))],
        [InlineKeyboardButton("DDOS ATTACK ❗️", callback_data=str(Dds))],
        [InlineKeyboardButton("PORT SCANNER 🔎", callback_data=str(sckn))],
        [InlineKeyboardButton("DNS LOOKUP 🔘", callback_data=str(dn))],
        [InlineKeyboardButton("SUBENT LOOKUP 🔎", callback_data=str(sub))],
        [InlineKeyboardButton("WEBSITE LINKS ™️", callback_data=str(lnke))],
        [InlineKeyboardButton("GO BACK 🔙", callback_data=str(bck))]]
    ms =  """  
-------------------
TRACKING AND HACKING DEPARTMENT ☑️
-------------------
    """
    okr = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{ms}", reply_markup=okr)
    return MAIN
def serh(update,context  ):
    query = update.callback_query
    Keyboard = [
        [InlineKeyboardButton("TIKTOK INFO 👁‍🗨", callback_data=str(tKin))],
        [InlineKeyboardButton("INSTAGRAM INFO 👁‍🗨", callback_data=str(insCK))],
        [InlineKeyboardButton("SEARCH ON GOOGLE 🔎", callback_data=str(gogl))],
        [InlineKeyboardButton("THE EMAIL IS LEAKED OR NOT ❓", callback_data=str(ck))],
        [InlineKeyboardButton("SEARCH FOR EMAIL ON WEBSITE 🔎", callback_data=str(TIK))],
        [InlineKeyboardButton("SEARCH FOR USER ON WEBSITE 🔎", callback_data=str(twCHK))],
        [InlineKeyboardButton("GO BACK 🔙", callback_data=str(bck))]
    ]
    okr = InlineKeyboardMarkup(Keyboard)
    ms = """
-------------------------
  INFORMATION SEARCH 👁‍🗨
-------------------------
    """
    query.edit_message_text(text=f"{ms}", reply_markup=okr)
    return MAIN
def trgm(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.bot.send_sticker(chat_id=query.message.chat_id,sticker='https://t.me/vv3ck/9')
def start(update, context: CallbackContext) -> None:
    global name , user_id
    user_id = update.effective_chat.id
    useID = str(user_id)
    update: Update
    name = update.message.from_user.first_name
    update.message.bot.send_message(chat_id=update.message.chat_id, text=f"Wait..", timeout=999999)
    try:
        if blokID in useID:
            msg = "اهلا برلين لايسمح لك بأستخدام البوت لاانك حرامي"
            update.message.bot.send_message(chat_id=update.message.chat_id, text=f"{msg}")
        elif blokID2 in useID:
            msg = "اهلا معجون لايسمح لك بأستخدام البوت لاانك حرامي"
            update.message.bot.send_message(chat_id=update.message.chat_id, text=f"{msg}")

        else:
            join = context.bot.get_chat_member(chat_id="@vv1ck", user_id=update.effective_chat.id)
            if (join.status == "kicked") or (join.status == "left"):
                ms = """
            يرجى الاشتراك بقناة المطور اولا ❤️
    Please subscribe to the channel
    @vv1ck
    
    /start  
                    """
                context.bot.send_message(user_id, f"{ms}")
            else:
                mss =f"""
    username : {name}
    ID : {useID}
    tg://user?id={user_id}
                """
                r.post(f'https://api.telegram.org/bot{TOKadmin}/sendMessage?chat_id={IDadmin}&text={mss}')
                msg = f"""
            time : {tim}
    
       Welcome  {name}  ❤️
    
      RESEARCH AND INVESTIGATION
    
    Here you will find some tools
    To help you Gather Information
    About A Person OR Check website
    رجاء اضغط هنا قبل الاستخدام 👇🏼:
    /help
                        """
                Keyboard = [
                    [InlineKeyboardButton("ترجمة الاوامر 🔘 ", callback_data=str(trgim))],
                    [InlineKeyboardButton("Bot channel 🖤", url="https://t.me/vv1ck"),
                    InlineKeyboardButton("Share bot 🖤", switch_inline_query_current_chat="")],
                    [InlineKeyboardButton("RANDOM TOOLS 🔘", callback_data=str(AS3))],
                    [InlineKeyboardButton("INFORMATION GATHERING TOOLS 🔘", callback_data=str(b7s))],
                    [InlineKeyboardButton("NETWORKING AND HACKING TOOLS 🔘", callback_data=str(hck))]]
                reply_markup = InlineKeyboardMarkup(Keyboard)
                update.message.bot.send_message(chat_id=update.message.chat_id,text=f"{msg} ",reply_markup=reply_markup,timeout=99999)
                return MAIN
    except telegram.error.BadRequest:
        msg = """
عذرا البوت لايعمل بالمجموعات!
Sorry, the bot does not work 
in groups!
@vv1ck
        """
        update.message.bot.send_message(chat_id=update.message.chat_id, text=f"{msg} ")
    except requests.exceptions.ConnectionError:
        update.message.bot.send_message(chat_id=update.message.chat_id, text=f"Please wait a bit and then tap /start")
    except telegram.error.TimedOut:
        update.message.bot.send_message(chat_id=update.message.chat_id, text=f"Please wait a bit and then tap /start")
def non(update,context  ):
    query = update.callback_query
    query.edit_message_text(text="{}".format(query.data))
def back(update,context  ):
    global name
    query = update.callback_query
    msg =  f"""
        time : {tim}

   Welcome  {name}  ❤️

  RESEARCH AND INVESTIGATION

Here you will find some tools
To help you Gather Information
About A Person OR Check website
رجاء اضغط هنا قبل الاستخدام 👇🏼:
/help
                """
    Keyboard = [
        [InlineKeyboardButton("ترجمة الاوامر 🔘 ", callback_data=str(trgim))],
        [InlineKeyboardButton("Bot channel 🖤", url="https://t.me/vv1ck"),
         InlineKeyboardButton("Share bot 🖤", switch_inline_query_current_chat="")],
        [InlineKeyboardButton("RANDOM TOOLS 🔘", callback_data=str(AS3))],
        [InlineKeyboardButton("INFORMATION GATHERING TOOLS 🔘", callback_data=str(b7s))],
        [InlineKeyboardButton("NETWORKING AND HACKING TOOLS 🔘", callback_data=str(hck))]]
    okr = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=okr)
    return MAIN
def help(update , context):
    ms = """
اهلا صديقي البوت مخصص للبحث عن المعلومات عن المواقع والمستخدمين

حسناً اظن بانك تعلم ما وظيفة البوت الان وماذا يفعل لذالك ارجوا منك عدم اللعب به 
البوت ليس اداة لفحص اليوزرات و الايميلات المتاحة 😉

استخدم البوت في وقت الحاجة فقط ☑️

ملاحظة البوت مجاني لا احلل لمن يبيعه

━━━━━━━━━━━━━
Hey my friend, the bot is for searching information about websites and users

Well I think you know what a bot is doing now and what it is doing so please don't play around with it
Use the robot only when needed ☑️

Note that the robot is free, not for sale

/start
"""
    update.message.reply_text(text=f"{ms}")
    return MAIN
def main() -> None:
    updater = Updater("1682874543:AAHHI8USuBLi1IJlU53R05dLTfDGDwTW_Zs", use_context=True)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start,run_async=True)],
        states={
            MAIN: [
                CallbackQueryHandler(tools, pattern='^' + str(TIK) + '$',run_async=True),
                CallbackQueryHandler(Twit, pattern='^' + str(twCHK) + '$',run_async=True),
                CallbackQueryHandler(trgm, pattern='^' + str(trgim) + '$',run_async=True),
                CallbackQueryHandler(serh, pattern='^' + str(b7s) + '$',run_async=True),
                CallbackQueryHandler(Aso3e, pattern='^' + str(AS3) + '$',run_async=True),
                CallbackQueryHandler(back, pattern='^' + str(bck) + '$',run_async=True),
                CallbackQueryHandler(checEml, pattern='^' + str(ck) + '$',run_async=True),
                CallbackQueryHandler(instU, pattern='^' + str(insCK) + '$',run_async=True),
                CallbackQueryHandler(hack, pattern='^' + str(hck) + '$',run_async=True),
                CallbackQueryHandler(ppi, pattern='^' + str(pi) + '$',run_async=True),
                CallbackQueryHandler(doos, pattern='^' + str(Dds) + '$',run_async=True),
                CallbackQueryHandler(scans, pattern='^' + str(sckn) + '$',run_async=True),
                CallbackQueryHandler(dne, pattern='^' + str(dn) + '$',run_async=True),
                CallbackQueryHandler(subD, pattern='^' + str(sub) + '$',run_async=True),
                CallbackQueryHandler(ling, pattern='^' + str(lnke) + '$',run_async=True),
                CallbackQueryHandler(gogle, pattern='^' + str(gogl) + '$',run_async=True),
                CallbackQueryHandler(TIKnfo, pattern='^' + str(tKin) + '$',run_async=True),
                CallbackQueryHandler(gtip, pattern='^' + str(gteip) + '$',run_async=True),
                CallbackQueryHandler(teleegg, pattern='^' + str(rde) + '$',run_async=True),
                CallbackQueryHandler(UR3, pattern='^' + str(HIur) + '$',run_async=True)]},
        fallbacks=[CommandHandler('start', start)],)
    dispatcher.add_handler(conv_handler)
    dp = updater.dispatcher
    hlp = CommandHandler('help', help, run_async=True)
    dp.add_handler(hlp)
    oke = CommandHandler('check', emils, run_async=True)
    dp.add_handler(oke)
    ins = CommandHandler('user', Login, run_async=True)
    dp.add_handler(ins)
    tle = CommandHandler('target', teleg , run_async=True)
    dp.add_handler(tle)
    io = CommandHandler('ip', ipp, run_async=True)
    dp.add_handler(io)
    esl = CommandHandler('email', SNPEML, run_async=True)
    dp.add_handler(esl)
    scr = CommandHandler('scanner', scanr, run_async=True)
    dp.add_handler(scr)
    dnss = CommandHandler("dns",ddns, run_async=True)
    dp.add_handler(dnss)
    sbdm = CommandHandler("sub", subdom, run_async=True)
    dp.add_handler(sbdm)
    lnk = CommandHandler("link", linkpge, run_async=True)
    dp.add_handler(lnk)
    glge = CommandHandler("google", Google, run_async=True)
    dp.add_handler(glge)
    tkIN = CommandHandler("tiktok", TIKinfo, run_async=True)
    dp.add_handler(tkIN)
    GTIP = CommandHandler("get_ip", gtIPP, run_async=True)
    dp.add_handler(GTIP)
    hidUL = CommandHandler("hide", UL1, run_async=True)
    dp.add_handler(hidUL)


    dispatcher.add_handler(CommandHandler('stqrt', start, run_async=True))
    updater.dispatcher.add_handler(CallbackQueryHandler(non))
    updater.start_polling(timeout=999999)
    updater.idle()

if __name__ == '__main__':
    main()
