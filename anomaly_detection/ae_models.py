import torch
import torch.nn as nn

class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(10, 5),
            nn.ReLU(),
            nn.Linear(5, 2)
        )
        self.decoder = nn.Sequential(
            nn.Linear(2, 5),
            nn.ReLU(),
            nn.Linear(5, 10),
            nn.Sigmoid()  # Using Sigmoid to ensure output values between 0 and 1
        )
    
    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

# Initialize the model
autoencoder = Autoencoder()
autoencoder.eval()  # Set the model to evaluation mode if not training

def ae_process_data(data_instance):
    """
    Processes a single data instance through the autoencoder.
    
    Parameters:
        data_instance (Data): The data instance (from Faust stream).
    
    Returns:
        tuple: A tuple containing the device_id and the reconstruction error.
    """
    result_dict = dict()
    # Convert list of features to a tensor with a batch dimension
    features_tensor = torch.tensor([data_instance.features], dtype=torch.float32)
    #data_instance['features']
    # Pass the data through the autoencoder
    reconstructed = autoencoder(features_tensor)
    
    # Calculate the reconstruction error (mean squared error)
    loss = nn.functional.mse_loss(reconstructed, features_tensor)
    result_dict['device_id'] = data_instance.id #data_instance['id']
    result_dict['reconstruction_loss'] = loss.item()

    return result_dict


if __name__ == '__main__':
    data_instance = {'id': 'device4_2060', 'features': [0.57, 0.52, 0.56, 0.45, 0.57, 0.48, 0.44, 0.48, 0.37, 0.46], 'log': {'temperature': 29, 'status': 'normal'}}
    #print(data_instance['id'])
    result = ae_process_data(data_instance)
    print(result)