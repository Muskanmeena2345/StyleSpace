import torch
import torch.nn as nn

class DesignGenerator(nn.Module):
    def __init__(self):
        super(DesignGenerator, self).__init__()
        self.fc1 = nn.Linear(100, 128)
        self.fc2 = nn.Linear(128, 256)
        self.fc3 = nn.Linear(256, 3 * 64 * 64)  # Assuming output is a 64x64 image with 3 channels

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.tanh(self.fc3(x))
        return x.view(-1, 3, 64, 64)

if __name__ == "__main__":
    generator = DesignGenerator()
    sample_input = torch.randn(1, 100)
    sample_output = generator(sample_input)
    print(sample_output.shape)
