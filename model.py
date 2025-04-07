import sklearn
import torch
from utils import load_train_test_datasets
from static import PREDICTOR_COLUMNS, TARGET_COLUMN, TARGET_CLASS_DICT
from learning_model import run_prediction,load_tensors,train_model,your_model
from data_preparation import extract


def load_model():
    model = torch.nn.Sequential(
        torch.nn.Linear(len(PREDICTOR_COLUMNS), 6),
        torch.nn.Linear(6, 12),
        torch.nn.Linear(12, 24),
        torch.nn.Linear(24, 12),
        torch.nn.Linear(12, 6),
        torch.nn.Linear(6, len(TARGET_CLASS_DICT))
    )
    model.load_state_dict(torch.load('model_weights.pth'))
    model.eval()  # 切换到评估模式
    return model

# 加载模型
loaded_model =

# 准备测试数据
_test_x_tensor = extract(5654104319)

# 进行预测
predictions = run_prediction(loaded_model, _test_x_tensor)

# 输出预测结果
print(predictions)