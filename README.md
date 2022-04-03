# Redis - Big Data
To run project, use these commands in order (Linux Ubuntu):  
- Run ClickAnalyzer Spark job in the background:  
    spark-submit --jars lib/spark-redis.jar ClickAnalyzer.py > ./click_count.log 2>&1 &  
- Or run ClickAnalyzer with the terminal:  
    spark-submit --jars lib/spark-redis.jar ClickAnalyzer.py  
- Next, open a new terminal (if ClickAnalyzer is not in the background) then run Django web server:
    python web/manage.py runserver  
  
Then go to the webpage at hosted localhost, click on the pictures to send click counts.
