from websrv import app

# time.sleep(10)
try:
    app.run(host="0.0.0.0",port=80)
except Exception as e:
    print "[*] ",e