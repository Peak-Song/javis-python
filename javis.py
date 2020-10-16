from src import root
from src.handler import ConfigHandler, GitHandler

root.info('javis back stage start...')

# 完成配置文件的生成或者读取, 完成程序全局变量设置
ConfigHandler.init()
# 按照配置中data目录完成git相关实例化
GitHandler.init()

# 启动flask服务

# 启动websocket服务


# 完成git的健康度检查
# 如果git健康, 设置
# 如果git尚未配置, 后台推送信息给前端, 前端进行配置

# 启动worker, 监视git健康状态, 如果git健康就开始同步数据, 提交数据

