
FTP Là Gì?

FTP là chữ viết tắt của File Transfer Protocol (Giao thức chuyển nhượng tập tin), đây là một giao thức giúp bạn dễ dàng trao đổi các dữ liệu giữa máy tính của bạn với host và ngược lại. Tại FTP, bạn sẽ có quyền quản lý toàn bộ các dữ liệu dạng tập tin và thư mục có trên host ngoại trừ database. Tất cả các gói host bạn mua có hỗ trợ control panel cPanel, DirectAdmin,…đều hỗ trợ sẵn FTP qua cổng kết nối 21.

FTP là một khái niệm rất quan trọng vì trong suốt thời gian bạn sử dụng host để làm website, có thể bạn sẽ cần sử dụng FTP nhiều hơn là dùng control panel của host vì nó sẽ giúp bạn tiện lợi hơn trong việc upload/quản lý các tập tin và thư mục trên host vì sử dụng tính năng File Manager có trong control panel đôi lúc hơi rườm rà và bất tiện, cũng như ở trên đó bạn sẽ không thấy các tập tin hệ thống có tên là .htaccess, nên chúng ta sẽ cần sử dụng FTP để quản lý dữ liệu trên ổ cứng của host.

VSFTPD Là Gì?

Hai chữ đầu tiên của vsftpd có nghĩa "very secure". VSFTPD là một FTP Server cho hệ thống Unix-like được phân phối bởi Red Hat Enterprise Linux. VSFTPD  được sử dụng rộng rãi trên Linux server, sử dụng VSFTPD đảm bảo cho chúng ta an toàn trước 99% lỗ hỏng bảo mật trên FTP Server.

Mô hình VSFTPD có các đặc điểm chính như sau:

Giữa tiến trình mang đặc quyền và tiến trình không mang đặc quyền có phan chia rõ ràng.

Các tiến trình được chạy trong chroot jail nhằm nâng cao bảo mật.

Chroot trên các hệ điều hành Unix là một công đoạn thay đổi thư mục root cho các tiến trình đang chạy hiện tại và các tiến trình con của nó.

- Tiến hành cài đặt.

 
            git clone https://github.com/letran3691/vsftp.git
    
- Phân quyên file         
    
            chmod +x vsftp/installpython3.6.sh
    
- Cài đặt python3.6

            ./vsftp/installpython3.6.sh
    
    
- Sau khi cài đặt python xong file shell sẽ tự đông gọi đến file Python để cài VSFTP
     
![image](https://user-images.githubusercontent.com/19284401/59593451-2bb67380-911c-11e9-8b8b-ff32b245336b.png)

 - Nhập 1 rồi Enter để cài đặt mới.
 
 ![image](https://user-images.githubusercontent.com/19284401/59593662-8c45b080-911c-11e9-8334-8be847e536ef.png)

- Quá trình cài đặt VSFTP bắt đầu

    - Trong quá trình cài đặt hệ thống sẽ cài đặt luôn ssl. Các bạn làm theo hướng dẫn

![image](https://user-images.githubusercontent.com/19284401/59733017-a0052a00-9276-11e9-85e0-8fd3a9d9a1dc.png)
         
     


![image](https://user-images.githubusercontent.com/19284401/59593900-fe1dfa00-911c-11e9-99bb-80c572497ab8.png)


- Quá trình cài đặt diễn ra rất nhanh. Đồng thời sẽ hiển thị ra ip public của bạn. IP nhé sẽ liên quan đến viêc các bạn NAT port vs ip này.

![image](https://user-images.githubusercontent.com/19284401/59594224-a59b2c80-911d-11e9-933f-a7a1e8f7ff56.png)

- IP public sẽ được input vào file cấu hình.
    - Các bạn chú ý đến
    
        - pasv_min_port: 
        
        - pasv_max_port:
        
- Khi NAT port các bạn nhớ NAT cả **range port** này nhé

- Như vậy là cài đặt và cấu hình VSFTP đã xong.              

- Giờ đến tạo user:
            
            ./vsftp/vsftp.py
    
    ![image](https://user-images.githubusercontent.com/19284401/59596153-5bb44580-9121-11e9-9ada-259b17277569.png)
    
- Nhập 2 để tạo tài khoản

    ![image](https://user-images.githubusercontent.com/19284401/59596433-e1d08c00-9121-11e9-837d-22945e6fac19.png)
    
    - Test tài khoản ftp:
        
        ![image](https://user-images.githubusercontent.com/19284401/59596532-18a6a200-9122-11e9-9d57-4701062ef11e.png)
        
    - Đây là các command user hỗ trợ
        
        ![image](https://user-images.githubusercontent.com/19284401/59596631-4ab80400-9122-11e9-9a09-d3ccdc1b9254.png)
        
    - Test upload bằng fileZilla
        
        - Các bạn chút ý khi đăng nhập bằng Filezilla nhớ tich chọn **Always trust** như trong hình, rOKồi nn **OK**.
    
        ![image](https://user-images.githubusercontent.com/19284401/59733193-3afe0400-9277-11e9-8572-072497caea4c.png)
    
        ![image](https://user-images.githubusercontent.com/19284401/59596939-ddf13980-9122-11e9-8485-4920981fdd94.png)
        
        ![image](https://user-images.githubusercontent.com/19284401/59597003-ffeabc00-9122-11e9-9c1f-f2b3f24317b9.png)
        
        ![image](https://user-images.githubusercontent.com/19284401/59597045-198c0380-9123-11e9-9d40-9958fd474d2a.png)

- Nhập 3 để xóa tài khoản

    Các bạn chú ý là có gì quan trọng thì nên backup lại nhé, gì khi xóa tài khoản sẽ sẽ xóa luôn cả thư mục của user đó.
    
    ![image](https://user-images.githubusercontent.com/19284401/59597280-9cad5980-9123-11e9-9c0e-e22c439c0781.png)
    
    ![image](https://user-images.githubusercontent.com/19284401/59597323-bcdd1880-9123-11e9-83e1-ccf38c921fcf.png)
    
    ![image](https://user-images.githubusercontent.com/19284401/59597399-ef871100-9123-11e9-8e98-a1afbe16f0a2.png)
    

   - Trường hợp các bạn không muốn xóa thư mục đó đi thì các bạn chỉ cần phần quyền lại cho thư mục là được.
            
            chmod -R root: /ftp/virtual/trunglv/
            

- Chúc các bạn thành công.

- Tham khảo:

    https://www.unixmen.com/install-vsftp-with-virtual-users-on-centos-rhel-scientific-linux-6-4/


       
        
    
        






    
    