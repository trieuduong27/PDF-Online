from deep_translator import GoogleTranslator

def translate_text(text, target_language='vi'):
    """
    Hàm nhận vào đoạn text và dịch sang ngôn ngữ đích (mặc định là tiếng Việt).
    Các mã ngôn ngữ phổ biến: 'vi' (Việt Nam), 'en' (Tiếng Anh), 'ja' (Tiếng Nhật)
    """
    if not text or text.strip() == "":
        return "Lỗi: Không có văn bản để dịch."

    try:
        # Thực hiện dịch bằng GoogleTranslator của deep_translator
        translation = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translation
        
    except Exception as e:
        return f"Đã xảy ra lỗi trong quá trình dịch: {str(e)}"

# Đoạn code test nhanh
if __name__ == "__main__":
    sample_text = "Software engineering is the systematic application of engineering approaches to the development of software."
    
    print("Văn bản gốc:", sample_text)
    print("\nĐang dịch sang tiếng Việt...")
    
    result = translate_text(sample_text, target_language='vi')
    print("Kết quả:", result)