from typing import List
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType,ArrayType,MapType
from pyspark.sql.functions import col,struct,when

from pyspark.sql.types import (IntegerType,
                               StringType,
                               DoubleType,
                               TimestampType)


schema = {
    # 'customer_shopping_data': StructType([
    'Sales_data': StructType([
        StructField("ORDERNUMBER", IntegerType(), True),
        StructField("QUANTITYORDERED", IntegerType(), True),
        StructField("PRICEEACH", DoubleType(), True),
        StructField("ORDERLINENUMBER", IntegerType(), True),
        StructField("SALES", DoubleType(), True),
        StructField("ORDERDATE", TimestampType(), True),
        StructField("STATUS", StringType(), True),
        StructField("QTR_ID", IntegerType(), True),
        StructField("MONTH_ID", IntegerType(), True),
        StructField("YEAR_ID", TimestampType(), True),
        StructField("PRODUCTLINE", StringType(), True),
        StructField("MSRP", IntegerType(), True),
        StructField("PRODUCTCODE", StringType(), True),
        StructField("CUSTOMERNAME", StringType(), True),
        StructField("PHONE", StringType(), True),
        StructField("ADDRESSLINE1", StringType(), True),
        StructField("ADDRESSLINE2", StringType(), True),
        StructField("CITY", StringType(), True),
        StructField("STATE", StringType(), True),
        StructField("POSTALCODE", IntegerType(), True),
        StructField("COUNTRY", StringType(), True),
        StructField("TERRITORY", StringType(), True),
        StructField("CONTACTLASTNAME", StringType(), True),
        StructField("CONTACTFIRSTNAME", StringType(), True),
        StructField("DEALSIZE", StringType(), True)


      ])
}
