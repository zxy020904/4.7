import sklearn
import torch
from utils import load_train_test_datasets
from static import PREDICTOR_COLUMNS, TARGET_COLUMN, TARGET_CLASS_DICT

def run_prediction(_model, x_tensor):
    # Given a model and input, predict the corresponding output
    with torch.no_grad():
        test_predict = _model(x_tensor)
        _, predicted_classes = torch.max(test_predict, 1)
    return predicted_classes

def calc_accuracy(_model, x_tensor, y_tensor):
    predicted_classes = run_prediction(_model, x_tensor)
    # Accuracy = Number of correct prediction / Number of items to be predicted
    return (predicted_classes == y_tensor).sum().item() / y_tensor.size(0)

def load_tensors():
    train_x, train_y, test_x, test_y = load_train_test_datasets()
    # Convert to PyTorch tensors
    _train_x_tensor, _test_x_tensor = torch.FloatTensor(train_x.to_numpy(dtype=float)), torch.FloatTensor(test_x.to_numpy(dtype=float))
    _train_y_tensor, _test_y_tensor = torch.LongTensor(train_y.to_numpy(dtype=float)), torch.LongTensor(test_y.to_numpy(dtype=float))
    return _train_x_tensor, _test_x_tensor, _train_y_tensor, _test_y_tensor

def train_model(x_tensor, y_tensor) -> torch.nn.Sequential:
    torch.manual_seed(5963)
    # Configurable: Your model structure
    model = torch.nn.Sequential(
        torch.nn.Linear(len(PREDICTOR_COLUMNS), 6),
        torch.nn.Linear(6, 12),
        torch.nn.Linear(12, 24),
        torch.nn.Linear(24, 12),
        torch.nn.Linear(12, 6),
        torch.nn.Linear(6, len(TARGET_CLASS_DICT))
    )
    # Cross Entropy Loss is used for classification
    loss_function = torch.nn.CrossEntropyLoss()

    # Configurable: Hyper-parameters
    num_epochs = 400
    learning_rate = 0.2
    # Configurable: optimizer
    optimizer = torch.optim.Adagrad(model.parameters(), lr=learning_rate)

    # Start training
    for epoch in range(num_epochs):
        optimizer.zero_grad() # Resets gradients
        train_predict = model(x_tensor)  # Make a prediction
        loss = loss_function(train_predict, y_tensor)  # Calculate loss
        loss.backward()  # Calculate gradient
        optimizer.step()  # Update weights using the graident
        if (epoch + 1) % (num_epochs/10) == 0:
            print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')
    return model





if __name__ == '__main__':
    train_x_tensor, test_x_tensor, train_y_tensor, test_y_tensor = load_tensors()
    your_model = train_model(train_x_tensor, train_y_tensor)
    print(f'Train accuracy: {calc_accuracy(your_model, train_x_tensor, train_y_tensor):.2%}')
    print(f'Test accuracy: {calc_accuracy(your_model, test_x_tensor, test_y_tensor):.2%}')
    torch.save(your_model.state_dict(), 'model_weights.pth')




