from pyspark.sql import sparkSession
import numpy as np
import pandas as pd
from pii import data_encryption, data_decryption
import matplotlib as mpl



spark = sparkSession.master("*").appName("Commit message change testing").getOrCreate()
df = spark.createDataFrame()
df.show()

spark.stop()


# *************************************************
"""
Replicate conflicts
1. Now I have made changes in query 1
2. I am query 2
3. I am query 3
4. I am query 4
5. I am query 5
6. Now I have made changes in query 6
7. I am query 7
"""
