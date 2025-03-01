import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from models.caption_model import EncoderCNN, DecoderRNN
from utils.data_loader import ImageCaptioningDataset

def load_data():
    image_paths = []
    captions = []
    
    # Example data format - replace with your actual data loading logic
    data = [
        ("image1.jpg", "This is a caption for image 1"),
        ("image2.jpg", "A description of image 2")
    ]
    
    for img_path, caption in data:
        image_paths.append(f'data/images/{img_path}')
        captions.append(caption)
    
    return image_paths, captions

def train(encoder, decoder, train_loader, criterion, encoder_optimizer, decoder_optimizer, device):
    encoder.train()
    decoder.train()
    total_loss = 0
    
    for images, captions in train_loader:
        images = images.to(device)
        captions = captions.to(device)
        
        encoder_optimizer.zero_grad()
        decoder_optimizer.zero_grad()
        
        features = encoder(images)
        outputs = decoder(features, captions)
        
        loss = criterion(outputs.view(-1, outputs.size(-1)), captions.view(-1))
        loss.backward()
        
        encoder_optimizer.step()
        decoder_optimizer.step()
        
        total_loss += loss.item()
    
    return total_loss / len(train_loader)

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Hyperparameters
    embed_size = 256
    hidden_size = 512
    vocab_size = 5000
    num_epochs = 10
    batch_size = 32
    learning_rate = 0.001
    
    # Load data
    image_paths, captions = load_data()
    dataset = ImageCaptioningDataset(image_paths, captions)
    train_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    
    # Initialize models
    encoder = EncoderCNN(embed_size).to(device)
    decoder = DecoderRNN(embed_size, hidden_size, vocab_size).to(device)
    
    # Initialize optimizers
    encoder_optimizer = torch.optim.Adam(encoder.parameters(), lr=learning_rate)
    decoder_optimizer = torch.optim.Adam(decoder.parameters(), lr=learning_rate)
    
    criterion = nn.CrossEntropyLoss()
    
    # Training loop
    for epoch in range(num_epochs):
        train_loss = train(encoder, decoder, train_loader, criterion,
                          encoder_optimizer, decoder_optimizer, device)
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {train_loss:.4f}")

if __name__ == "__main__":
    main()
