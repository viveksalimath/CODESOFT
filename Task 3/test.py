import torch
from models.caption_model import EncoderCNN, DecoderRNN

def test_models():
    embed_size = 256
    hidden_size = 512
    vocab_size = 5000
    
    # Test encoder
    encoder = EncoderCNN(embed_size)
    decoder = DecoderRNN(embed_size, hidden_size, vocab_size)
    
    # Create dummy input
    dummy_image = torch.randn(1, 3, 224, 224)
    dummy_caption = torch.randint(0, vocab_size, (1, 10))
    
    # Test forward pass
    features = encoder(dummy_image)
    outputs = decoder(features, dummy_caption)
    
    print("Models initialized successfully!")
    print(f"Feature shape: {features.shape}")
    print(f"Output shape: {outputs.shape}")

if __name__ == "__main__":
    test_models()
