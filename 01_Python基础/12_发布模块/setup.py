from distutils.core import setup

setup(name="study_message",  # 包名
      version="1.0",  # 版本
      description="study 发送和接收信息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="xujinshan",  # 作者
      author_email="xujinshan361@163.com",  # 作者邮箱
      url="www.baidu.com",  # 主页
      py_modules=["study_message.receive_message",
                  "study_message.send_message"]
      # py_modules = ["study_message.send_message"]
)