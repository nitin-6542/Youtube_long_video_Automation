from selenium import webdriver 
import time
import random
from gtts import gTTS
import threading
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from moviepy.editor import AudioFileClip, ImageClip
from moviepy.editor import *
from selenium.webdriver.chrome.options import Options
from PIL import Image, ImageSequence
from PIL import ImageDraw
from PIL import ImageFont
from selenium.webdriver.common.action_chains import ActionChains
import os
options = Options()
options.headless = False
options.add_argument('--window-size=1920x1080')
gif1 = Image.open("girl.gif")
im3= Image.open("girlz.png")
k=1
l=['GXChain','LockTrip']
while k<=30:
        
        i=str(k)
        driver = webdriver.Chrome(executable_path="chromedriver",options=options)
        language = 'en'
        driver.maximize_window()
        driver.get("https://www.coingecko.com/en/crypto-gainers-losers")
        name=driver.find_element(By.XPATH,"//div[1]/div[1]/table[1]/tbody[1]/tr["+i+"]/td[1]").text
        volume=driver.find_element(By.XPATH,"//div[1]/div[1]/table[1]/tbody[1]/tr["+i+"]/td[2]").text
        price=driver.find_element(By.XPATH,"//div[1]/div[1]/table[1]/tbody[1]/tr["+i+"]/td[3]").text
        percentage=driver.find_element(By.XPATH,"//div[1]/div[1]/table[1]/tbody[1]/tr["+i+"]/td[4]").text
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,"//div[1]/div[1]/table[1]/tbody[1]/tr["+i+"]/td[1]/div[1]/div[2]/a[1]/span[1]").click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 110)")
        name=name.split("\n")
        name=name[1]
        
        title="Bytecoin token full details and where to buy and sell it and list of exchanges"
        tag="Bytecoin token buy,Bytecoin token,Bytecoin token price,Bytecoin token buy and sell,Bytecoin taoken in trust wallet,Bytecoin token using pancakeswap,how to buy and sell Bytecoin token,how to use pancakeswap,how to use trustwallet,Bytecoin,Bytecoin,Bytecoin,Bytecoin to php,crypto Bytecoin how to sell,Bytecoin how to buy and sell,Bytecoin token sell on trustwallet"
        desc="""Bytecoin token full details and where to buy and sell it.dont forget to like and subscribe the channel
        #Bytecoin
        #pancakeswap 
        #uniswap
        #token
        #uniswap"""
        
        tag=tag.replace("Bytecoin",name)
        title=title.replace("Bytecoin",name)
        desc=desc.replace("Bytecoin",name)
        dirr=name.replace("/","")
        dirr=name.replace(" ","")
        mid=""
        if dirr not in l:
                l.append(dirr)
                os.mkdir(dirr)
                driver.save_screenshot(dirr+"/ss.png")
                im = Image.open(dirr+"/ss.png")
                im2=Image.open("text.png")
                left = 250
                top = 150
                right = 1100
                bottom = 800
                im1 = im.crop((left, top, right, bottom))
                
                newsize = (400, 500)
                im2=im2.resize(newsize)
                im1.paste(im2, (400, 50))
                im3=im3.resize(newsize)
                im1.paste(im3, (0, 250),mask=im3)
                newsize = (1280, 720)
                im1=im1.resize(newsize)
                
                im1.save(dirr+"/wallpaper.png")
                likes=driver.find_element(By.XPATH,"(//div[@class='tw-block tw-inline-flex tw-py-0.5 tw-h-5 tw-items-center tw-px-2 tw-rounded-md tw-text-xs tw-font-medium tw-bg-gray-100 tw-text-gray-800 tw-mb-1 md:tw-mb-0 dark:tw-text-white dark:tw-bg-white dark:tw-bg-opacity-5'])[1]").text

                driver.execute_script("window.scrollTo(0, 2550)")
                driver.implicitly_wait(5)
                rows = driver.find_elements(By.XPATH,"//table[1]/tbody/tr")
                
                time.sleep(5)
                driver.save_screenshot(dirr+"/ss1.png")
                background = Image.open(dirr+"/ss.png")
                frames = []
                for gif1_frame in ImageSequence.Iterator(gif1):
                    frame = background.copy()
                    frame.paste(gif1_frame,(-200,600), mask=gif1_frame.convert("LA"))
                    frames.append(frame)
                frames[0].save(dirr+"/out1.gif", save_all=True, append_images=frames[1:], loop=0)
                frames = []
                background = Image.open(dirr+"/ss1.png")
                for gif1_frame in ImageSequence.Iterator(gif1):
                    frame = background.copy()
                    frame.paste(gif1_frame,(-200,600), mask=gif1_frame.convert("LA"))
                    frames.append(frame)
                frames[0].save(dirr+"/out2.gif", save_all=True, append_images=frames[1:], loop=0)

                print(name,volume,price,percentage,likes)
                
                tlikes=likes.replace(",","")
                tlikes=tlikes[3:]
                lk=""
                for i in tlikes:
                    if i.isnumeric():
                        lk=lk+i
                    else:
                        break
                if int(lk)>5000:
                        t="Coin Likes is greater than 5000 we can say that the coin is best going "
                elif int(lk)>1000:
                        t="Coin Likes is greater than 1000 we can say that the coin is average  going "
                else:
                        t="Coin likes is less than 1000 we can assume token is in struggle stage invest carefully Trust Score is low "

                fname=name+".txt"
                print(name)
                s=" Hello Guys , Today  we are Going to know ,  About the "+ name +" Token "+"24 hours Volume and percentage increased and how many people likes"+"Currently in 24 Hours volume of token is "+ volume +" and current price is "+ price +" In 24 Hours the price of the coins increases upto "+ percentage +"And currently "+likes[3:]+" "+t+" The most important part is contract address copy that and use it on exchange platform to search the token if it is not availabe then you can direct search on this token om these exchanges list is given in the end of video"
                s1=" this token you can trade the token on these websites" + "link of the exchanges are in description "+"Do not  forget to like and subscribe the youtube channel Thank you "
                
                print(len(rows))
                print(l)
                ex=[]
                links=[]
                try:
                        for i in range(1,len(rows)-1):
                                ex.append(driver.find_element(By.XPATH,"//table[1]/tbody[2]/tr["+str(i)+"]/td[2]").text)
                                links.append(driver.find_element(By.XPATH,"//table[1]/tbody[2]/tr["+str(i)+"]/td[2]/div[1]/a[1]").get_attribute('href'))
                        print(links)
                        exname=" ".join(ex)
                        s1=" this token you can trade  on these  websites "+ exname + "link of the exchanges are in description "+"Do not  forget to like and subscribe the youtube channel Thank you "
                        lnames="\n".join(links)
                        mid=mid+" "+name+" "+volume+" "+price+" "+percentage+" "+lnames+" "+"\n"+lnames+"\n"+"Disclaimer This video is for educational purpose i am not suggesting you to buy this coin this video is just a procedure for where you can buy this coin means all exchanges"
                        
                                
                                
                        
                        myobj = gTTS(text=s, lang=language, slow=False)
                        myobj1 = gTTS(text=s1, lang=language, slow=False)
                        myobj.save(dirr+"/welcomee.mp3")
                        myobj1.save(dirr+"/welcome.mp3")
                        
                        os.popen("ffmpeg -y -stream_loop -1 -i "+dirr+"/out1.gif -i "+dirr+"/welcomee.mp3  -r 24 -shortest -acodec copy  "+dirr+"/output1.mp4 -threads 8")
                        os.popen("ffmpeg -y -stream_loop -1 -i "+dirr+"/out2.gif -i "+dirr+"/welcome.mp3  -r 24 -shortest -acodec copy  "+dirr+"/output2.mp4 -threads 8")
                        time.sleep(5)
                        os.popen("(for %i in ("+dirr+"/*.mp4) do @echo file '%i') > "+dirr+"/mylist.txt")
                        os.popen("ffmpeg -f concat -safe 0 -i /"+dirr+"/mylist.txt -c copy outputf.mp4")
                        os.popen("copy m.bat "+dirr+"")
                        os.popen("/"+dirr+"/m.bat")
                        
                        time.sleep(2)
                        f = open(dirr+"/tags.txt", "x")
                        f = open(dirr+"/tags.txt", "w")
                        f.write(tag)
                        f.close()
                        f = open(dirr+"/title.txt", "x")
                        f = open(dirr+"/title.txt", "w")
                        f.write(title)
                        f.close()
                        f=open(dirr+"/title.txt","a")
                        f.write(desc)
                        f.close()
                        f=open(dirr+"/title.txt","a")
                        f.write(mid)
                        f.close()
                        
                        print("file Created and audio ")
                        time.sleep(5)
                        driver.close()
                        print(k)
                        k=k+1


                except:
                        print(links)
                        lnames="\n".join(links)
                        mid=mid+" "+name+" "+volume+" "+price+" "+percentage+" "+likes+" "+"\n"+lnames+"\n"+"Disclaimer This video is for educational purpose i am not suggesting you to buy this coin this video is just a procedure for where you can buy this coin means all exchanges"   
                        exname=" ".join(ex)
                        s1=" this token you can trade  on these websites "+ exname + "link of the exchanges are in description "+"Do not  forget to like and subscribe the youtube channel Thank you "

                        myobj = gTTS(text=s, lang=language, slow=False)
                        myobj1 = gTTS(text=s1, lang=language, slow=False)
                        myobj.save(dirr+"/welcomee.mp3")
                        myobj1.save(dirr+"/welcome.mp3")
                        
                        os.popen("ffmpeg -y -stream_loop -1 -i "+dirr+"/out1.gif -i "+dirr+"/welcomee.mp3  -r 24 -shortest -acodec copy  "+dirr+"/output1.mp4 -threads 8")
                        os.popen("ffmpeg -y -stream_loop -1 -i "+dirr+"/out2.gif -i "+dirr+"/welcome.mp3  -r 24 -shortest -acodec copy  "+dirr+"/output2.mp4 -threads 8")

                        time.sleep(5)
                        os.popen("(for %i in ("+dirr+"/*.mp4) do @echo file '%i') > "+dirr+"/mylist.txt")
                        os.popen("ffmpeg -f concat -safe 0 -i /"+dirr+"/mylist.txt -c copy outputf.mp4")
                        os.popen("copy m.bat "+dirr+"")
                        os.popen("/"+dirr+"/m.bat")
                        
                        time.sleep(2)
                        f = open(dirr+"/tags.txt", "x")
                        f = open(dirr+"/tags.txt", "w")
                        f.write(tag)
                        f.close()
                        f = open(dirr+"/title.txt", "x")
                        f = open(dirr+"/title.txt", "w")
                        f.write(title)
                        f.close()
                        f=open(dirr+"/title.txt","a")
                        f.write(desc)
                        f.close()
                        f=open(dirr+"/title.txt","a")
                        f.write(mid)
                        f.close()
                        
                        print("file Created and audio ")
                        time.sleep(5)
                        driver.close()
                        print(k)
                        k=k+1
                        print(l)
        else:
                k=k+1

