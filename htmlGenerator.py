file_name = input("Enter File Name : ")
date = input("Date : ")
src = input("Iframe Code : ")
url = './src/'+file_name+'.html'
html = '\n<div class="l"><a href='+url+'>'+date+'</a></div>'
with open(url, 'w',encoding='utf-8') as fp:
    pass
    fp.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>'+date+'</title><style>body{padding:0;margin:0;background:#fff;overflow:hidden}iframe{width:100%;position:absolute;margin:auto;background-color:#999;top:50%;left:50%;transform:translate(-50%,-50%)}nav{background-color:rgb(93, 179, 164);display:flex;justify-content:space-between;color:aliceblue;font-family:Arial,Helvetica,sans-serif;letter-spacing:2px;position:fixed;width:100%}nav button{transform:rotate(180deg);background:none;outline:none;border:none;font-size:25px;margin-left:10px;background-color:rgba(0,81,119,0.473);margin-top:15px;margin-bottom:15px;border-radius:5px}button:active{opacity:0.5;background-color:rgba(0,81,119,0.473)}a{text-decoration:none;color:aliceblue}.l{height:100vh;width:100%}</style></head><body> <nav class="header"> <button class="back-btn"><a href="../index.html">➜</a></button><div><h1>'+date+'</h1></div><div></div> </nav><div class="l">'+src+'</div></body></html>')
    print("Created File at "+url)
with open('./index.html','a',encoding='utf-8') as index :
    index.write(html)
    print("Added in ./index") 
print("DONE")