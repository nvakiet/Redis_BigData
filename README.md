# Redis - Big Data
Ho Chi Minh University of Science - Computer Science - K19 - Introduction to Big Data   
Project: Research about Redis and make a program to demonstrate a use-case of Redis  
Group name: KKAP  
Members:  
- Ngô Văn Anh Kiệt
- Triệu Nguyên Phát
- Phùng Anh Khoa
- Ngô Huy Anh

See our reports in "Research reports" folder.  

To run the demo, use these commands in order (on Linux Ubuntu):  
- Run ClickAnalyzer Spark job in the background:  
    spark-submit --jars lib/spark-redis.jar ClickAnalyzer.py > ./click_count.log 2>&1 &  
- Or run ClickAnalyzer with the terminal:  
    spark-submit --jars lib/spark-redis.jar ClickAnalyzer.py  
- Next, open a new terminal (if ClickAnalyzer is not in the background) then run Django web server:
    python web/manage.py runserver  
Then go to the webpage at hosted localhost, click on the pictures to send click counts.  
Make sure you have installed Apache Spark, Redis server and all the python packages in requirements.txt
