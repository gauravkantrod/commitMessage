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
1. I am query 1
2. I am query 2
4. I am query 4
"""
