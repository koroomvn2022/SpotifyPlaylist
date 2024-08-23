# Tạo một playlist trên spotify

## Giới Thiệu

Bài tập này tạo ra một playlist trên Spotify chứa 100 bài hát từ Billboard Hot 100. Quy trình bao gồm việc lấy thông tin xác thực từ Spotify, thu thập dữ liệu từ Billboard, và tạo ra một playlist trên Spotify.

## Quy Trình

1. **Tạo ứng dụng trên Spotify Developer**: Đầu tiên, tạo một ứng dụng trên Spotify Developer để lấy `client_id` và `client_secret`.

2. **Lấy ủy quyền**: Sử dụng `client_id` và `client_secret` để lấy Access Token từ Spotify (xem tệp `get_credential`).

3. **Thu thập dữ liệu từ Billboard**: Sử dụng thư viện Requests và BeautifulSoup để thu thập 100 bài hát từ Billboard Hot 100 (xem tệp `get_track`).

4. **Tạo danh sách phát trên Spotify**: Cuối cùng, sử dụng thư viện Requests để tạo một danh sách phát trên Spotify chứa 100 bài hát đã thu thập từ Billboard (xem tệp `create_playlist`).

## Công Nghệ

- **Spotify API**: Được sử dụng để lấy thông tin xác thực và tạo danh sách phát.
- **Requests**: Thư viện Python được sử dụng để gửi yêu cầu HTTP.
- **BeautifulSoup**: Thư viện Python được sử dụng để phân tích cú pháp HTML và XML, giúp thu thập dữ liệu từ Billboard.