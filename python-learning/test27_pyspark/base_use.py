from pyspark import SparkConf,SparkContext

conf = SparkConf().setAppName("test_spark_app").setMaster("local[*]")
sc = SparkContext(conf = conf)

print(sc.version)
list = [1,2,3,4]
rdd = sc.parallelize(list)

print(rdd.collect())