import logging
import traceback
import pytest

#进行捕捉异常
def raises(func):
    def bb(*args):
        #进行捕获异常
        with pytest.raises(BaseException) as error:
            func(*args)
        #获取pytest异常后的信息:粗略的
        logging.error(error.traceback.getcrashentry())
        #获取pytest异常后的信息:详细的
        # logging.error(error.getrepr())

    traceback.format_exc()

    return bb

