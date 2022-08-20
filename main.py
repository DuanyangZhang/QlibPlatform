import qlib
from qlib.constant import REG_CN
provider_uri = "/data/qlib_data/cn_data_ak"  # target_dir
qlib.init(provider_uri=provider_uri, region=REG_CN)