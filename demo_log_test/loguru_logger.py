
from loguru import logger
#打印一条日志,日志级别由低到高：颜色逐渐加深debug、info、warning、success、 error
# debug : 调试日志
# info ：普通日志
# warning ：警告日志
# success ：成功日志
# error ：错误日志
#打印级别低的，高的也会显示，如打印debug，其他的4个都会显示，如果打印error只显示error日志
logger.debug('hello world')

logger.debug("这是一条Debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

#输出到文件：add()方法
logger.add("a.log", format="{time} {level} {message}", level="INFO")

logger.info("这是一条info日志")
logger.debug("这是一条Debug日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

#时间格式化
logger.add("a.log", format="{time:YYYY-MM-DD at HH:MM:SS} {level} {message}", level="SUCCESS")
logger.debug("这是一条Debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

#传入参数格式化
logger.info("我的名字叫{},今天星期{}",'张三','一')

#文件保存
logger.add("file_1.log", rotation="500 MB") # 文件过大就会重新生成一个文件
logger.add("file_2.log", rotation="12:00") # 每天12点创建新文件
logger.add("file_3.log", rotation="1 week") # 文件时间过长就会创建新文件
logger.add("file_X.log", retention="10 days") # 一段时间后会清空
logger.add("file_Y.log", compression="zip") # 保存zip格式