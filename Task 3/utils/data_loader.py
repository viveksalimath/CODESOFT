from torch.utils.data import Dataset
from PIL import Image
import torchvision.transforms as transforms

class ImageCaptioningDataset(Dataset):
    def __init__(self, image_paths, captions, transform=None):
        self.image_paths = image_paths
        self.captions = captions
        self.transform = transform or transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                               std=[0.229, 0.224, 0.225])
        ])
        
    def __len__(self):
        return len(self.image_paths)
    
    def __getitem__(self, idx):
        image = Image.open(self.image_paths[idx]).convert('RGB')
        image = self.transform(image)
        caption = self.captions[idx]
        return image, caption
