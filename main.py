
with open('programmi.txt','r') as fp:
    link = 'https://isapplesiliconready.com/it?apps='
    app=fp.readline()[:-1]
    i=0
    while(app):
        if(i>0):
            link+=','
        app=app.translate({ord(i):'%20' for i in app if i==' '})
        link+=app
        app=fp.readline()[:-1]
        i+=1
    print(link)