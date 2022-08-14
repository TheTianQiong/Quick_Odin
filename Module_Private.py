def GetDocumentPath():
    import os
    return os.path.join(os.path.expanduser("~"),'Documents')

def mkdir(path):#新建文件夹存放图片
    import os
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

class File:
    def Add():
        address = GetDocumentPath() + "\OdinFiles\OdinLink\OdinLinkCfg.xml"#获取地址
        CheckFileUp = open(address,"w+")#晕，几行指令解决问题……
        CheckFileUpContent = CheckFileUp.readlines()
        if CheckFileUpContent == []:
            FileExample = ['<?xml version="1.0"?>','<LinkConfig xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">','  <PinCode></PinCode>','  <NetCardName></NetCardName>','  <SubNetCardName></SubNetCardName>','  <DeviceName></DeviceName>',"  <FileCachePath>" + GetDocumentPath() + "\OdinFiles\OdinLink\FileCache\</FileCachePath>",'  <FluencyMode></FluencyMode>','  <Language>zh-CN.xaml</Language>','  <CacheSize></CacheSize>','  <NoFirstLoad>true</NoFirstLoad>','  <AsClient>false</AsClient>','  <OpenLog>false</OpenLog>','  <ID></ID>','  <AutoConnect>false</AutoConnect>','  <HotSpotName></HotSpotName>','  <HotSpotCode></HotSpotCode>','</LinkConfig>',' ']
            for i in range(len(FileExample)):
                CheckFileUp.write(FileExample[i] + '\n')
        CheckFileUp.close()#这可太行了！
        #def“open”函数减轻RUN文件的大小