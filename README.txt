
This is the API testing for Fongfu Pi-Face-Video, V1.0
by Chin-Chun, Lee duke@fongfu.com.tw

To use the script, please follow instruction below:

安裝下載此程式
git clone https://github.com/chinchunli/Pi-Face-Video.git

1.設定機台名稱，第19行中設定， PI_DI = ‘xxxxx’

2.設定錄影時間，第22行中設定，TOTAL_SEC = 錄影時間 /多少秒

3.設定是否自動重新開機並重新錄製，設定開機後自動執行程式，
	> sudo nano /etc/rc.local
        在最後一行加入:
        加入python /home/pi/Pi-Face-Video/VideoRecorder.py
	
	
	完成後輸入 ctrl + x 
	按 Y 再輸入一次enter
	開機設定完成
4.調成拍攝角度。
5.@sudo reboot 開始錄製。
