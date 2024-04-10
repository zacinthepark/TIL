# def apply_augmentations(img_array):
#     augmentations = []
    
#     # Blur
#     blur = cv2.blur(img_array, (5, 5))
    
#     # Gaussian Blur
#     gaussian_blur = cv2.GaussianBlur(img_array, (5, 5), 0)
    
#     # Sharpen
#     kernel_sharpen = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
#     sharpen = cv2.filter2D(img_array, -1, kernel_sharpen)
    
#     # Contrast Enhancement
#     contrast = exposure.equalize_adapthist(img_array/255.0)
#     contrast = np.clip(contrast * 255.0, 0, 255).astype('uint8')
    
#     # Canny Edge Detection
#     edges = cv2.Canny(img_array, astype(np.uint8), 100, 200)
    
#     # Corner Detection (Harris Corner)
#     gray = cv2.cvtColor(img_array, astype(np.uint8), cv2.COLOR_RGB2GRAY)
#     corners = cv2.cornerHarris(gray, 2, 3, 0.04)
#     corners = cv2.dilate(corners, None)
#     corners = np.stack((corners,) * 3, axis=-1) # 3채널 이미지로 변환
    
#     # Add augmented images to list
#     augmentations.extend([blur, gaussian_blur, sharpen, contrast, edges, corners])
    
#     return augmentations

# def augment_dataset(dataset):
#     augmented_data = []
#     for img_array, label in tqdm(dataset, total=len(dataset)):
#         augmentations = apply_augmentations(img_array)
#         for aug_img in augmentations:
#             augmented_data.append([aug_img, label])
#             # augmented_data.append((aug_img, label))
#     return np.array(augmented_data, dtype=object)

# augmented_train_dataset = augment_dataset(train_dataset)
