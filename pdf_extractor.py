import PyPDF2
import os

def extract_text_from_pdf(file_path):
    
    extracted_text = ""
    
    if not os.path.exists(file_path):
        return "Lỗi: Không tìm thấy file PDF."

    try:
        # Mở file PDF dưới dạng đọc nhị phân (rb)
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Lặp qua từng trang và trích xuất chữ
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                extracted_text += page.extract_text() + "\n"
                
        return extracted_text.strip()
    
    except Exception as e:
        return f"Đã xảy ra lỗi trong quá trình đọc PDF: {str(e)}"

# Tesr chức năng trích xuất từ file PDF
if __name__ == "__main__":
    # Bạn hãy copy một file PDF bất kỳ vào thư mục dự án và đổi tên thành 'sample.pdf'
    sample_pdf_path = "bao_cao.pdf" 
    
    print("Đang xử lý file PDF...")
    result = extract_text_from_pdf(sample_pdf_path)
    
    print("\n--- KẾT QUẢ TRÍCH XUẤT ---")
    print(result)