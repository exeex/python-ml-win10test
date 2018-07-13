# 機器學習/深度學習Python Windows環境架設
文:cswu / xray0h@gmail.com / cswu@gapp.nthu.edu.tw

## 官方版Python與Anaconda版Python

有很多高速運算的Python套件都是用C語言寫的。而官方版Python並沒有包含編譯好的Library或C編譯器，這會造成很多套件安裝Error。要搞定這些Error往往會耗費大量的時間。因此，對於打算用Python作數值運算的工程師，筆者強烈建議各位使用Anaconda版的Python取代Python官方提供的安裝檔。

Anaconda是一個Python的組合包，集合了大部分你會用到的套件，而且都幫你編譯好了，可以節省大量自己編譯Debug的時間。當然，當你想要節省容量的時候，不會想要安裝這個組合包裡的所有東西，對於有這樣需求的使用者，可以使用精簡版的Miniconda，以手動的方式安裝必要的套件。以下是這兩個套件的下載連結

[下載Anaconda](https://www.anaconda.com/download/)  (包含許多Data Science常用的套件，在個人電腦使用建議用這個)  
[下載Miniconda](https://conda.io/miniconda.html) (乾淨的精簡版，在多使用者的Deep Learning工作站，建議用這個)  

以下安裝文件是寫給Windows的使用者，各位下載好後不要太過興奮，就一路用預設設定按完所有安裝流程。  
我這邊**建議各位讀者按照以下的方式安裝**，以省下日後各種不必要的麻煩。



## Windows作業系統Anaconda安裝流程
1. 安裝對象設定

如果只有你使用這台電腦，可以選Just me，使用預設路徑安裝  
如果是一個多人環境，可以選All Users


![](https://2.bp.blogspot.com/-Fr7AmrUayJk/WnFjQdyabfI/AAAAAAAACt4/ub1HxrR_0qYsoRDHwECo9u739B1N6Q-6QCEwYBhgL/s640/9.JPG)

2. 安裝路徑設定

前一個步驟選Just me選項的話，可以使用預設路徑安裝，然後跳到步驟3.  
若你選All User選項請參考如下設定：  

    C:\Anaconda3                #好選擇
    D:\Anaconda3                #好選擇
    C:\ProgramData\Anaconda3    #預設路徑，非常不建議，會有資料夾權限問題，導致套件裝不進去
    C:\Program Files\Anaconda3  #非常不建議，同上
![建議不要使用預設路徑安裝](https://i.stack.imgur.com/lzkSW.png)




3. PATH環境變數設定

勾選選項一，可以讓anaconda能夠直接在命令提示字元中被呼叫  
勾選選項二，以anaconda的python為預設的python直譯器  
建議兩個都勾，比較省事  

![](https://4.bp.blogspot.com/-Rca9z7q2X2A/WnFjLiaAo-I/AAAAAAAACtw/KFK77JVMMH8jZaBynlDWvu4iAEiIGn2IQCEwYBhgL/s640/10.JPG)


註：內文的警告是說，勾選選項一可能會和你之前安裝的python衝突，如果你沒有裝過任何python可以忽略該警告。  


4. 剩下一路點到完  
# 環境測試與套件安裝

裝了不一定能用，請下載測試腳本  
並依照以下測試流程，確定所有套件都能夠成功運行  

https://github.com/exeex/python-ml-win10test


## Test1 PATH路徑測試

你可以直接雙擊test1_path.bat執行測試腳本  
這會列出你安裝的程式的路徑，若無，則需重設PATH環境變數  
正常情形如下圖所示  

![path_test_pass.JPG](https://github.com/exeex/python-ml-win10test/blob/master/test_pass_img/path_test_pass.JPG?raw=true)

## Test2 matplotlib測試

測試Python是否正常運行，以及是否有正確安裝numpy, matplotlib等套件  
如果你是使用miniconda，這邊需要先安裝上述的那兩個套件  
開啟命令提示字元後輸入下列指令安裝  

    conda install numpy matplotlib

裝完後，運行測試腳本結果應如下  

![plot_test_pass.jpg](https://github.com/exeex/python-ml-win10test/blob/master/test_pass_img/plot_test_pass.jpg?raw=true)

## Test3 Tensorflow測試

tensorflow是最大宗的深度學習套件，照理來說是要裝一下的  
tensorflow不包含在預設Anaconda/Miniconda套件內，需手動安裝  
開啟命令提示字元後輸入下列指令安裝(這是安裝CPU版，GPU版安裝詳見[此文章](https://mark-down-now.blogspot.com/2018/01/tensorflow-gpu-x-windows-10.html))

    pip install tensorflow tensorboard
 
裝完後，運行測試腳本結果應如下  

![tf_test_pass.jpg](https://github.com/exeex/python-ml-win10test/blob/master/test_pass_img/tf_test_pass.jpg?raw=true)

## Test4 Pytorch測試

Pytorch是目前市面上最彈性最好用的深度學習框架。如果你是資料工程師，主要工作是研發，而不是在手機或商用的高流量伺服器上開發，那你應該使用Pytorch而不是tensorflow。  

pytorch不包含在預設Anaconda/Miniconda套件內，需手動安裝  
開啟命令提示字元後輸入下列指令安裝(這是安裝CPU版)  

    conda install pytorch-cpu -c pytorch 
    pip3 install torchvision

裝完後，運行測試腳本結果應如下  

![pytorch_test_pass.jpg](https://github.com/exeex/python-ml-win10test/blob/master/test_pass_img/pytorch_test_pass.jpg?raw=true)

## Test5 scikit-learn測試

scikit-learn是目前最泛用的機器學習套件，你可以在sklearn中找到各式各樣現成的機器學習模型來使用（比如SVM）。  
不過對於神經網路/深度學習模型，我還是建議你使用tensorflow或pytorch等套件。  
安裝指令如下：

    conda install scikit-learn
![skl_test_pass.jpg](https://github.com/exeex/python-ml-win10test/blob/master/test_pass_img/skl_test_pass.jpg?raw=true)


